"""
File for LLM return functions
- End phase
"""
from state import State
from session import Session

def end_conversation(session: Session):
    # finalize conversation, save all necessary data
    session.state.reset_all()
    session.state = State()
    return 1

def end_phase(session: Session):
    
    if session.state.get_current_phase() == 6:
        return end_conversation(session)
    
    return 0
    
