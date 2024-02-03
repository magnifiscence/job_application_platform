// JobListings.js
import React, { useState, useEffect } from 'react';
import { getJobListings } from './apiService';

const JobListings = () => {
    const [listings, setListings] = useState([]);

    useEffect(() => {
        getJobListings()
            .then(response => setListings(response.data))
            .catch(error => console.error('Error fetching job listings:', error));
    }, []);

    return (
        <div>
            <h2>Job Listings</h2>
            <ul>
                {listings.map(listing => (
                    <li key={listing.id}>{listing.title} - {listing.description}</li>
                ))}
            </ul>
        </div>
    );
}

export default JobListings;
