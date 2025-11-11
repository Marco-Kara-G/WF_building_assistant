from sqlalchemy.orm import Session


class WarframeDAO:
    def __init__(self,session:Session):
        self.session = session


