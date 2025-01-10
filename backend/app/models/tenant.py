from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin

class Tenant(Base, TimestampMixin):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    domain = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    
    # Subscription status
    subscription_plan = Column(String, nullable=True)
    subscription_status = Column(String, nullable=True)
    
    # Relationships
    users = relationship("User", back_populates="tenant")
    
    def __repr__(self):
        return f"<Tenant {self.name}>"