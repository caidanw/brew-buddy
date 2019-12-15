import React, {Component, Fragment} from 'react';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {getCapitals} from '../../actions/capitals';
import {getClosestBreweries} from '../../actions/breweries';

class Search extends Component {
    static propTypes = {
        capitals: PropTypes.array.isRequired,
        getCapitals: PropTypes.func.isRequired,
        getClosestBreweries: PropTypes.func.isRequired
    };

    componentDidMount() {
        this.props.getCapitals();
    }

    onSubmit = e => {
        e.preventDefault();
        this.props.getClosestBreweries(this.refs.capitalId.value);
    };

    render() {
        return (
            <Fragment>
                <div className="form-group">
                    <h3>Capital</h3>
                    <form className="form-inline my-2 " onSubmit={this.onSubmit}>
                        <select className="custom-select mr-2" ref="capitalId">
                            { this.props.capitals.map(capital => (
                                <option key={capital.id} value={capital.id}>{capital.name}, {capital.capital}</option>
                            ))}
                        </select>
                        <button className="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
                    </form>
                </div>
            </Fragment>
        );
    }
}

const mapStateToProps = state => ({
    capitals: state.capitals.capitals
});

export default connect(mapStateToProps, { getCapitals, getClosestBreweries })(Search);
