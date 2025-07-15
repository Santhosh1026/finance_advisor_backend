from app.database import Base, engine
from app.models import user, credit

Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")