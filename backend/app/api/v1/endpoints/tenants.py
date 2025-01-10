from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.models import User, Tenant  # Changed from app.db.models

router = APIRouter()

@router.get("/", response_model=List[schemas.Tenant])
def read_tenants(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_active_user),  # Changed from models.User
) -> Any:
    """
    Retrieve tenants.
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    tenants = db.query(Tenant).offset(skip).limit(limit).all()  # Changed from models.Tenant
    return tenants

@router.post("/", response_model=schemas.Tenant)
def create_tenant(
    *,
    db: Session = Depends(deps.get_db),
    tenant_in: schemas.TenantCreate,
    current_user: User = Depends(deps.get_current_active_user),  # Changed
) -> Any:
    """
    Create new tenant.
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    tenant = Tenant(  # Changed from models.Tenant
        name=tenant_in.name,
        domain=tenant_in.domain,
        is_active=tenant_in.is_active,
        subscription_plan=tenant_in.subscription_plan,
        subscription_status=tenant_in.subscription_status,
    )
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant

@router.get("/{tenant_id}", response_model=schemas.Tenant)
def read_tenant(
    tenant_id: int,
    current_user: User = Depends(deps.get_current_active_user),  # Changed
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get tenant by ID.
    """
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()  # Changed
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    if not current_user.is_superuser and tenant.id != current_user.tenant_id:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return tenant