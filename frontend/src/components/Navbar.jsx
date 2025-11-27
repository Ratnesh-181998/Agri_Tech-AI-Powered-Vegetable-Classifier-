import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="nav-container">
                <Link to="/" className="nav-logo">
                    🍅 Ninjacart AI
                </Link>
                <div className="nav-menu">
                    <Link to="/" className="nav-link">Home</Link>
                    <Link to="/vegetables" className="nav-link">Vegetables</Link>
                    <Link to="/classifier" className="nav-link">Classifier</Link>
                    <Link to="/about" className="nav-link">About</Link>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
