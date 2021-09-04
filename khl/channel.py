from abc import ABC
from typing import Dict

from .gateway import Requestable
from .interface import LazyLoadable
from .user import User


class Channel(LazyLoadable, Requestable, ABC):
    """
    Interface, represents a channel where messages flowing
    """
    pass


class TextChannel(Channel):
    """
    `Standard Object`

    Text chat channels in guild
    """
    id: str
    name: str
    user_id: str
    guild_id: str
    topic: str
    is_category: int
    parent_id: str
    level: int
    slow_mode: int
    type: int
    permission_overwrites: list
    permission_users: list
    permission_sync: int

    def __init__(self, **kwargs):
        self.id: str = kwargs.get('id')
        self.name: str = kwargs.get('name')
        self.user_id: str = kwargs.get('user_id')
        self.guild_id: str = kwargs.get('guild_id')
        self.topic: str = kwargs.get('topic')
        self.is_category: int = kwargs.get('is_category')
        self.parent_id: str = kwargs.get('parent_id')
        self.level: int = kwargs.get('level')
        self.slow_mode: int = kwargs.get('slow_mode')
        self.type: int = kwargs.get('type')
        self.permission_overwrites: list = kwargs.get('permission_overwrites')
        self.permission_users: list = kwargs.get('permission_users')
        self.permission_sync: int = kwargs.get('permission_sync')

        self._loaded = kwargs.get('_lazy_loaded_', False)
        self.gate = kwargs.get('_gate_')

    async def load(self):
        pass


class VoiceChannel(Channel):
    """
    Voice chat channel in guild

    a placeholder now for future design/adaption
    """

    async def load(self):
        pass


class PrivateChannel(Channel):
    """
    Private chat channel
    """

    code: str
    last_read_time: int
    latest_msg_time: int
    unread_count: int
    is_friend: bool
    is_blocked: bool
    is_target_blocked: bool
    target_info: User

    def __init__(self, **kwargs):
        self.code: str = kwargs.get('code')
        self.last_read_time: int = kwargs.get('last_read_time')
        self.latest_msg_time: int = kwargs.get('latest_msg_time')
        self.unread_count: int = kwargs.get('unread_count')
        self.is_friend: bool = kwargs.get('is_friend')
        self.is_blocked: bool = kwargs.get('is_blocked')
        self.is_target_blocked: bool = kwargs.get('is_target_blocked')
        self.target_info: Dict = kwargs.get('target_info')

        self._loaded = kwargs.get('_lazy_loaded_', False)
        self._gate = kwargs.get('_gate_')

    async def load(self):
        pass

    @property
    def target_user_id(self) -> str:
        return self.target_info.get('id') if self.target_info else None

    @property
    def target_user_name(self) -> str:
        return self.target_info.get('username') if self.target_info else None

    @property
    def is_target_user_online(self) -> bool:
        return self.target_info.get('online') if self.target_info else None

    @property
    def target_user_avatar(self) -> str:
        return self.target_info.get('avatar') if self.target_info else None