import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import JobListings from './JobListings';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route exact path="/job-listings" component={JobListings} />
	        <Route exact path="/user-profile" component={UserProfile} />
	        <Route exact path="/application-form" component={ApplicationForm} />
                {/* Add more routes for user profiles, application forms, etc. */}
            </Switch>
        </Router>
    );
}

export default App;

