from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class PaymentRecord(BaseModel):
    payment_id: int
    tenant_id: int
    payment_type: Literal['monthly_dues', 'property_tax']
    sent_date: datetime
    received_date: datetime
    method: Literal['check', 'card']
    payment_received: bool = False

class Maintenance(BaseModel):
    job_id: int
    work_type: str
    job_name: str
    condo_id: Optional[int]
    work_location: str = 'complex'
    completed_timestamp: Optional[datetime]

class ScheduledMaintenance(Maintenance):
    scheduled_date: datetime
    contractor: str
    notes: Optional[str]
    payment_amount: int
    payment_sent: bool = False
    