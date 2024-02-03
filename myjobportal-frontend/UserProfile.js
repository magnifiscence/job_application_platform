// UserProfile.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const UserProfile = () => {
    const [user, setUser] = useState(null);
    const { userId } = useParams();

    useEffect(() => {
        axios.get(`http://localhost:8000/users/${userId}/`)
            .then(response => setUser(response.data))
            .catch(error => console.error('Error fetching user:', error));
    }, [userId]);

    return (
        <div>
            {user && (
                <div>
                    <h2>User Profile</h2>
                    <p>Name: {user.name}</p>
                    <p>Email: {user.email}</p>
                    {/* Add more user details */}
                </div>
            )}
        </div>
    );
}

export default UserProfile;
