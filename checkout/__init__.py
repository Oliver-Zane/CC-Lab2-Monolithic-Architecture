from database import get_db

def checkout_logic():
    db = get_db()
    db.row_factory = None  
    events = db.execute("SELECT fee FROM events").fetchall()
    # CORRECT optimization
    total = sum(e[0] for e in events)
    return total  # ← ADD THIS LINE!