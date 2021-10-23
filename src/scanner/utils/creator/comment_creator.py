from src.scanner.utils.creator.__extra__ import *
from src.scanner.utils.creator.base import BaseCreator


class COMMENTCreator(BaseCreator):

    @property
    def states(self):
        return [
            {
                'id': 14
            },
            {
                'id': 15
            },
            {
                'id': 16
            },
            {
                'id': 17,
                'end': True,
                'token_type': TokenType.COMMENT
            },
            {
                'id': 18
            },
            {
                'id': 19,
                'end': True,
                'token_type': TokenType.COMMENT,
                'roll_back': True
            },
            {
                'id': 20,
                'error_type': ErrorType.UNCLOSED_COMMENT
            },
            {
                'id': 21,
                'error_type': ErrorType.INVALID_INPUT,
                'roll_back': True
            }
        ]

    @property
    def transitions(self):
        return [
            {'state_src_id': self.INITIAL_STATE_ID, 'state_dst_id': 14, 'symbols': SLASH},
            {'state_src_id': 14, 'state_dst_id': 15, 'symbols': STAR},
            {'state_src_id': 15, 'state_dst_id': 16, 'symbols': STAR},
            {'state_src_id': 16, 'state_dst_id': 16, 'symbols': STAR},
            {'state_src_id': 16, 'state_dst_id': 17, 'symbols': SLASH},
            {'state_src_id': 14, 'state_dst_id': 18, 'symbols': SLASH},
            {'state_src_id': 18, 'state_dst_id': 19, 'symbols': EOF + NEW_LINE},
            {'state_src_id': 15, 'state_dst_id': 20, 'symbols': EOF},
            {'state_src_id': 15, 'state_dst_id': 15, 'symbols': STAR + EOF, 'type': TransitionType.EXCLUDE},
            {'state_src_id': 16, 'state_dst_id': 15, 'symbols': STAR + EOF, 'type': TransitionType.EXCLUDE},
            {'state_src_id': 14, 'state_dst_id': 21, 'symbols': SLASH + STAR, 'type': TransitionType.EXCLUDE},
            {'state_src_id': 18, 'state_dst_id': 18, 'symbols': EOF + NEW_LINE, 'type': TransitionType.EXCLUDE}
        ]