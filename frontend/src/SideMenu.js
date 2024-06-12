import React from 'react';

const SideMenu = ({ isMenuOpen, toggleMenu }) => (
    <div className={`side-menu ${isMenuOpen ? 'open' : ''}`}>
        <div className="hamburger-background">
            <img 
                src="hamburger-icon.png" 
                className={`hamburger ${isMenuOpen ? 'no-background' : ''}`}
                onClick={toggleMenu}
                alt="Hamburger Icon"
            />
        </div>
        <div className={`menu-container ${isMenuOpen ? 'open' : ''}`}>
            <div className="menu"><p>View Schedule</p></div>
            <div className="menu"><p>SchedulEase</p></div>
            <div className="menu"><p>Explore</p></div>
        </div>
    </div>
);

export default SideMenu;
