import asyncio
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models import User, Tenant
from app.core.security import get_password_hash

async def create_first_superuser():
    db = SessionLocal()
    try:
        # Create initial tenant
        tenant = Tenant(
            name="Admin Tenant",
            domain="admin.roundtable.com",
            is_active=True,
            subscription_plan="enterprise",
            subscription_status="active"
        )
        db.add(tenant)
        db.commit()
        db.refresh(tenant)

        # Create superuser
        superuser = User(
            email="admin@roundtable.com",
            hashed_password=get_password_hash("admin123"),  # Change this password!
            full_name="Admin User",
            is_active=True,
            is_superuser=True,
            tenant_id=tenant.id
        )
        db.add(superuser)
        db.commit()
        
        print("Superuser and tenant created successfully!")
        print("Email: admin@roundtable.com")
        print("Password: admin123")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(create_first_superuser())