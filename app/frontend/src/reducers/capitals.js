import {GET_CAPITALS} from '../actions/types';

const initialState = {
    capitals: []
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_CAPITALS:
            return {
                ...state,
                capitals: action.payload
            };
        default:
            return state;
    }
}
