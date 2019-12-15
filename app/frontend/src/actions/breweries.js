import axios from 'axios';

import {GET_BREWERIES, GET_CLOSEST_BREWERIES} from './types';

export const getBreweries = () => dispatch => {
    axios.get('/api/breweries/')
        .then(res => {
            dispatch({
                type: GET_BREWERIES,
                payload: res.data
            });
        }).catch(error => console.log(error));
};

export const getClosestBreweries = capitalId => dispatch => {
    axios.get(`/api/breweries/closest/${capitalId}`)
        .then(res => {
            dispatch({
                type: GET_CLOSEST_BREWERIES,
                payload: res.data
            });
        }).catch(error => console.log(error));
};
