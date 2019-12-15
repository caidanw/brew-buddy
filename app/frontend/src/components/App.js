import React, {Component, Fragment} from 'react';
import ReadDOM from 'react-dom';

import Header from './layout/Header';
import Dashboard from './breweries/Dashboard';

import {Provider} from 'react-redux';
import store from '../store';

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Fragment>
                    <Header/>
                    <div className="container">
                        <Dashboard/>
                    </div>
                </Fragment>
            </Provider>
        );
    }
}

ReadDOM.render(<App />, document.getElementById('app'));
