import {GET_BREWERIES, GET_CLOSEST_BREWERIES} from '../actions/types';

const initialState = {
    breweries: []
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_BREWERIES:
            return {
                ...state,
                breweries: action.payload
            };
        case GET_CLOSEST_BREWERIES:
            return {
                ...state,
                breweries: action.payload
            };
        default:
            return state;
    }
}
