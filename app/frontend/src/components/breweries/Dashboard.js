import React, {Fragment} from 'react';
import Search from './Search';
import Breweries from './Breweries';

export default function Dashboard() {
    return (
        <Fragment>
            <Search />
            <Breweries />
        </Fragment>
    )
}
