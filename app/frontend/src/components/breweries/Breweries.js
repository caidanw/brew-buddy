import React, {Component, Fragment} from 'react';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {getBreweries} from '../../actions/breweries';

class Breweries extends Component {
    static propTypes = {
        breweries: PropTypes.array.isRequired,
        getBreweries: PropTypes.func.isRequired
    };

    componentDidMount() {
        this.props.getBreweries();
    }

    render() {
        return (
            <Fragment>
                <h3>Breweries</h3>
                <table className="table table-striped">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Type</th>
                        <th>Street</th>
                        <th>City</th>
                        <th>State</th>
                        <th>Postal</th>
                        <th>Country</th>
                        <th>Longitude</th>
                        <th>Latitude</th>
                        <th>Phone</th>
                        <th>Website</th>
                        <th>Last Updated</th>
                    </tr>
                    </thead>
                    <tbody>
                    { this.props.breweries.map(brewery => (
                        <tr key={brewery.id}>
                            <td>{brewery.id}</td>
                            <td>{brewery.name}</td>
                            <td>{brewery.brewery_type}</td>
                            <td>{brewery.street}</td>
                            <td>{brewery.city}</td>
                            <td>{brewery.state}</td>
                            <td>{brewery.postal_code}</td>
                            <td>{brewery.country}</td>
                            <td>{brewery.longitude}</td>
                            <td>{brewery.latitude}</td>
                            <td>{brewery.phone}</td>
                            <td>{brewery.website_url}</td>
                            <td>{brewery.updated_at}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </Fragment>
        );
    }
}

const mapStateToProps = state => ({
    breweries: state.breweries.breweries
});

export default connect(mapStateToProps, { getBreweries })(Breweries);
