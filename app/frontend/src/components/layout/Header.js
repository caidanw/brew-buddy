import React, {Component, Fragment} from 'react';

class Header extends Component {
    render() {
        return (
            <Fragment>
                <nav className="navbar navbar-expand-sm navbar-light bg-light">
                    <a className="navbar-brand" href="#">Brew Buddy</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor03"
                            aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"/>
                    </button>
                </nav>
                <br />
            </Fragment>
        );
    }
}

export default Header;
