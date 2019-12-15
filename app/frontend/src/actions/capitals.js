import axios from "axios";

import {GET_CAPITALS} from "./types";

export const getCapitals = () => dispatch => {
    axios.get('/api/capitals/')
        .then(res => {
            dispatch({
                type: GET_CAPITALS,
                payload: res.data
            });
        }).catch(error => console.log(error));
};
