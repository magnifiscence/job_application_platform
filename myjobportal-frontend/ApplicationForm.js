// ApplicationForm.js
import React, { useState } from 'react';
import { createApplication } from './apiService';

const ApplicationForm = () => {
    const [formData, setFormData] = useState({ jobListingId: '', applicantId: '', coverLetter: '' });

    const handleSubmit = (e) => {
        e.preventDefault();
        createApplication(formData)
            .then(response => {
                // Handle successful submission
                console.log('Application submitted successfully', response.data);
            })
            .catch(error => {
                // Handle error
                console.error('Error submitting application:', error);
            });
    }

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    }

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="jobListingId">Job Listing ID:</label>
                <input type="text" id="jobListingId" name="jobListingId" onChange={handleChange} />
            </div>
            <div>
                <label htmlFor="applicantId">Applicant ID:</label>
                <input type="text" id="applicantId" name="applicantId" onChange={handleChange} />
            </div>
            <div>
                <label htmlFor="coverLetter">Cover Letter:</label>
                <textarea id="coverLetter" name="coverLetter" onChange={handleChange} />
            </div>
            <button type="submit">Submit Application</button>
        </form>
    );
}

export default ApplicationForm;
