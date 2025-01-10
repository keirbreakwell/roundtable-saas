from pydantic import BaseModel
from typing import Optional

class TenantBase(BaseModel):
    name: str
    domain: str
    is_active: bool = True
    subscription_plan: Optional[str] = None
    subscription_status: Optional[str] = None

class TenantCreate(TenantBase):
    pass

class TenantUpdate(TenantBase):
    name: Optional[str] = None
    domain: Optional[str] = None
    is_active: Optional[bool] = None

class TenantInDBBase(TenantBase):
    id: int

    class Config:
        from_attributes = True

class Tenant(TenantInDBBase):
    pass

class TenantInDB(TenantInDBBase):
    pass