from librepos.models import MenuGroup
from . import EntityRepository


class MenuGroupRepository(EntityRepository[MenuGroup]):
    def __init__(self):
        super().__init__(MenuGroup)

    @staticmethod
    def get_active_groups() -> list[MenuGroup]:
        return MenuGroup.query.filter_by(active=True).all()

    @staticmethod
    def list_groups_by_category(category_id: int) -> list[MenuGroup]:
        return MenuGroup.query.filter_by(category_id=category_id).all()
