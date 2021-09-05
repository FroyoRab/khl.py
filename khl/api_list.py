import functools
import inspect
import logging
import re
from typing import Dict, Callable

log = logging.getLogger(__name__)


class _Req:
    def __init__(self, method: str, route: str, params: Dict):
        self.method = method
        self.route = route
        self.params = params


def req(method: str):
    def _method(func: Callable):
        @functools.wraps(func)
        def req_maker(*args, **kwargs) -> _Req:
            param_names = list(inspect.signature(func).parameters.keys())
            for i in range(len(args)):
                kwargs[param_names[i]] = args[i]
            route = re.sub(r'(?<!^)(?=[A-Z])', '-', func.__qualname__).lower().replace('.', '/')
            return _Req(method, route, kwargs)

        return req_maker

    return _method


class Guild:

    @staticmethod
    @req('GET')
    def list(
    ):
        ...

    @staticmethod
    @req('GET')
    def view(
            guild_id
    ):
        ...

    @staticmethod
    @req('GET')
    def userList(
            guild_id,
            channel_id,
            search,
            role_id,
            mobile_verified,
            active_time,
            joined_at,
            page,
            page_size,
    ):
        ...

    @staticmethod
    @req('POST')
    def nickname(
            guild_id,
            nickname,
            user_id,
    ):
        ...

    @staticmethod
    @req('POST')
    def leave(
            guild_id
    ):
        ...

    @staticmethod
    @req('POST')
    def kickout(
            guild_id,
            target_id
    ):
        ...


class GuildMute:

    @staticmethod
    @req('GET')
    def list(
            guild_id,
            return_type
    ):
        ...

    @staticmethod
    @req('POST')
    def create(
            guild_id,
            user_id,
            type,
    ):
        ...

    @staticmethod
    @req('POST')
    def delete(
            guild_id,
            user_id,
            type,
    ):
        ...


class Channel:

    @staticmethod
    @req('GET')
    def list(
            guild_id
    ):
        ...

    @staticmethod
    @req('GET')
    def view(
            target_id
    ):
        ...

    @staticmethod
    @req('POST')
    def create(
            guild_id,
            parent_id,
            name,
            type,
            limit_amount,
            voice_quality,
    ):
        ...

    @staticmethod
    @req('POST')
    def delete(
            channel_id
    ):
        ...

    @staticmethod
    @req('POST')
    def moveUser(
            target_id,
            user_ids
    ):
        ...


class ChannelRole:

    @staticmethod
    @req('GET')
    def index(
            channel_id
    ):
        ...

    @staticmethod
    @req('POST')
    def create(
            channel_id,
            type,
            value,
    ):
        ...

    @staticmethod
    @req('POST')
    def update(
            channel_id,
            type,
            value,
            allow,
            deny,
    ):
        ...

    @staticmethod
    @req('POST')
    def delete(
            channel_id,
            type,
            value,
    ):
        ...


class Message:

    @staticmethod
    @req('GET')
    def list(
            target_id,
            msg_id,
            pin,
            flag,
    ):
        ...

    @staticmethod
    @req('POST')
    def create(
            type,
            target_id,
            content,
            quote,
            nonce,
            temp_target_id,
    ):
        ...

    @staticmethod
    @req('POST')
    def update(
            msg_id,
            content,
            quote,
            temp_target_id,
    ):
        ...

    @staticmethod
    @req('POST')
    def delete(
            msg_id,
    ):
        ...

    @staticmethod
    @req('GET')
    def reactionList(
            msg_id,
            emoji
    ):
        ...

    @staticmethod
    @req('POST')
    def addReaction(
            msg_id,
            emoji
    ):
        ...

    @staticmethod
    @req('POST')
    def deleteReaction(
            msg_id,
            emoji,
            user_id
    ):
        ...

    @staticmethod
    @req('POST')
    def addReaction(
            msg_id,
            emoji
    ):
        ...

    @staticmethod
    @req('POST')
    def addReaction(
            msg_id,
            emoji
    ):
        ...


class UserChat:

    @staticmethod
    @req('GET')
    def list(
    ):
        ...

    @staticmethod
    @req('GET')
    def view(
            chat_code
    ):
        ...

    @staticmethod
    @req('POST')
    def create(
            target_id
    ):
        ...

    @staticmethod
    @req('POST')
    def delete(
            chat_code
    ):
        ...


class DirectMessage:

    @staticmethod
    @req('GET')
    def list(
            chat_code,
            target_id,
            msg_id,
            flag,
    ):
        ...

    @staticmethod
    @req('POST')
    def create(
            type,
            target_id,
            chat_code,
            content,
            quote,
            nonce,
    ):
        ...

    @staticmethod
    @req('POST')
    def update(
            msg_id,
            content,
            quote,
    ):
        ...

    @staticmethod
    @req('POST')
    def delete(
            msg_id
    ):
        ...

    @staticmethod
    @req('GET')
    def reactionList(
            msg_id,
            emoji
    ):
        ...

    @staticmethod
    @req('POST')
    def addReaction(
            msg_id,
            emoji
    ):
        ...

    @staticmethod
    @req('POST')
    def deleteReaction(
            msg_id,
            emoji
    ):
        ...


class Gateway:

    @staticmethod
    @req('GET')
    def index(
            compress
    ):
        ...
