import React, { useEffect } from 'react';

// eslint-disable-next-line react/prop-types
export default function EmbeddedSite({passData}) {
  useEffect(() => {
   
    const iframe = document.querySelector('iframe');

    // Wait for the iframe to load
    iframe.addEventListener('load', () => {
      // Send a message to the iframe after it has loaded
      iframe.contentWindow.postMessage(
        JSON.stringify({
          event: passData ? passData : "no message",
          status: true,
        }),
        'http://localhost:3000'
      );
      console.log(`%c sent data`, 'color: red')
      return
    });

    // Listen for messages from the iframe
    window.addEventListener('message', (event) => {
      console.log('event', event.data.message);
    });

    return () => {
      // Clean up event listeners if the component unmounts
      iframe.removeEventListener('load', () => {});
      window.removeEventListener('message', () => {});
    };
  });

  return (
    <div>
      {/* Embedding another website using an iframe */}
      <iframe
        id="myIframe"
        src="http://localhost:3000"
        height="300"
        width="400"
        title="Iframe Example"
      ></iframe>
    </div>
  );
}
