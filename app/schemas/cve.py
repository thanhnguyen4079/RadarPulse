from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field

class AffectedSoftware(BaseModel):
    # Software affected by CVE
    vendor: str
    product: str
    versions: list[str] = []
    version_start: Optional[str] = None
    version_end: Optional[str] = None

class RawCVE(BaseModel):
    """Raw data from NVD_API"""
    cve_id: str
    source: str = "NVD"
    description: str
    severity: Optional[str] = None
    cvss_score: Optional[float] = None
    cvss_vector: Optional[str] = None
    cwe_id: Optional[str] = None
    cwe_name: Optional[str] = None
    affected_software: list[AffectedSoftware] = []
    references: list[dict] = []
    published_date: Optional[datetime] = None
    last_modified: Optional[datetime] = None

class ProcessedCVE(BaseModel):
    """CVE after LLM enrichment"""
    cve_id: str
    source: str = "NVD"

     # Severity
    severity: Optional[str] = Field(
        default=None,
        description="CRITICAL, HIGH, MEDIUM, LOW",
    )
    cvss_score: Optional[float] = Field(
        default=None, ge=0.0, le=10.0,
    )
    cvss_vector: Optional[str] = None

    # Classification
    cwe_id: Optional[str] = None
    cwe_name: Optional[str] = Field(
        default=None,
        description="SQL Injection, XSS, Buffer Overflow, etc.",
    )
    # Affected software
    affected_software: list[AffectedSoftware] = []

    # Text content
    description: str
    summary: Optional[str] = Field(
        default=None,
        description="LLM-generated concise summary",
    )
    remediation: Optional[str] = Field(
        default=None,
        description="LLM-generated fix recommendation",
    )

    # References
    references: list[dict] = []

    # Dates
    published_date: Optional[datetime] = None
    last_modified: Optional[datetime] = None

# API response

# StackAudit