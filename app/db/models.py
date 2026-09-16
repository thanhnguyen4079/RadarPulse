from datetime import datetime, timezone
from sqlalchemy import (
    Column, Integer, String, Float, 
    JSON, DateTime, Text, Index,
)
from pgvector.sqlalchemy import Vector
from app.db.session import Base
from app.config import get_settings

settings = get_settings()

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    
    id = Column(Integer, primary_key = True, index = True)

    # CVE identity
    cve_id = Column(String, unique = True, index = True, nullable = False)
    source = Column(String, default = "NVD")

    # Severity
    severity = Column(String, index = True) # CRITICAL, HIGH, MEDIUM, LOW
    cvss_score = Column(Float, nullable = True) # 0.0 - 10.0
    cvss_vector = Column(String, nullable = True) # # CVSS:3.1/AV:N/AC:L/...

    # Classification
    cwe_id = Column(String, nullable = True, index = True) #CWE-89
    cwe_name = Column(String, nullable = True) # SQL injection

    # Affected software
    affected_software = Column(JSON, default = list)
    # Format: [{"vendor": "Django", "product": "Django", "versions": ["5.0","5.0.1"]}]

    # Description
    summary = Column(Text, nullable = True)  # LLM-generated short summary
    description = Column(Text, nullable = True)  
    remediation = Column(Text, nullable = True) # LLM-generated fix suggestion

    # References
    references = Column(JSON, default = list)
    # Format: [{"url": "https://...", "type": "PATCH"}]

    # Dates
    published_date = Column(DateTime(timezone = True), nullable = True)
    last_modified = Column(DateTime(timezone=True), nullable = True)

    # Embedding
    embedding = Column(Vector(settings.embedding_dim))

    # Internal timestamps
    created_at = Column(
        DateTime(timezone= True),
        default = lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        Index("ix_severity_cvss", "severity", "cvss_score")
    )