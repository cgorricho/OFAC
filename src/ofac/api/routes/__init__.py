"""API route handlers.

Routes:
- screening: POST /screenings/batch, POST /screenings/single
- data: GET /data/status, POST /data/refresh
- health: GET /health
"""

from ofac.api.routes import health

__all__ = ["health"]
