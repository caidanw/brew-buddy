import React, {Component, Fragment} from 'react';
import ReadDOM from 'react-dom';

import Header from './components/layout/Header';
import Dashboard from './components/breweries/Dashboard';

import {Provider} from 'react-redux';
import store from './store';

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Fragment>
                    <Header/>
                    <div className="m-5">
                        <Dashboard/>
                    </div>
                </Fragment>
            </Provider>
        );
    }
}

ReadDOM.render(<App />, document.getElementById('app'));
