import {combineReducers} from 'redux';
import breweries from './breweries';
import capitals from './capitals';

export default combineReducers({
    breweries,
    capitals
});
