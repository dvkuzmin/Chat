from classic.app.errors import AppError


class UserNotFound(AppError):
    msg_template = "NO such user"
    code = 'chat.user_not_found'


class NotOwnerError(AppError):
    msg_template = "User is not chat owner"
    code = 'chat.owner_error'


class ChatNotFound(AppError):
    msg_template = "Chat does not exist"
    code = 'chat.chat_not_found'


class NoRightsError(AppError):
    msg_template = "User has no rights"
    code = 'chat.user_no_rights'


class NoMessages(AppError):
    msg_template = "No messages in chat"
    code = 'chat.no_messages'

