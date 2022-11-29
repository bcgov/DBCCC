import React, { useRef, useEffect, useState } from 'react';

import Pin from './Pin.js';

import './Routes.css';


export default function Routes(props) {

  // const [open, setOpen] = useState(false);

  if (!props.open) {
    return (
      <button className="open-routes"
        onClick={() => props.setRoutesOpen(true)}
      >Add Route</button>
    )
  }

  return (
    <div className="routes">
      <button className="close-routes"
        onClick={() => props.setRoutesOpen(false)}
      >X</button>

      <div className="starting">
        <div className="anchor">A</div>
        <div className="text">
          <h4>Starting Location</h4>
          <div className="options">
            <div className="option" onClick={props.setStartToLocation}>
              <div className="pin-icon">&gt;</div>
              current location
            </div>
            <span className="option">
              Or
            </span>
            <div className="option">
              <div><Pin role="start" /></div>
              <div>Drop this point</div>
            </div>
          </div>
        </div>
      </div>

      <div className="starting">
        <div className="anchor">B</div>
        <div className="text">
          <h4>Destination</h4>
          <div className="options">
            <div className="option">
              <div><Pin role="end" /></div>
              <div>Drop this point</div>
            </div>
          </div>
        </div>
      </div>

      <div className="notification">
        <h4>Notification Email</h4>
        <p>Notify me of any new road events along this route</p>
        <div>
          <input type="text" />
        </div>
        <h3>+ Add Route</h3>
      </div>

    </div>
  )
};