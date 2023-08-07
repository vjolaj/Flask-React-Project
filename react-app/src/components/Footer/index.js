import React from 'react';
import "./Footer.css";


function Footer() {
    return (
        <div id='footer-wrapper'>
            <div id='footer-content'>
                <h2>The Developers</h2>
                <div id='developers'>
                    <div className='developer'>
                        <img src="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/mexican.png"/>
                        <div>
                            <h3>Vjola Jorgji</h3>
                            <a href="https://github.com/vjolaj" target="_blank" rel="noopener noreferrer">GitHub</a>
                        </div>
                    </div>
                    <div className='developer'>
                        <img src='https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/sushi.png'/>
                        <div>
                            <h3>Calvin Kwon</h3>
                            <a href="https://github.com/kwoncalvin" target="_blank" rel="noopener noreferrer">GitHub</a>
                        </div>
                    </div>
                    <div className='developer'>
                        <img src="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/pizza.png"/>
                        <div>
                            <h3>Genesis Mendes</h3>
                            <a href="https://github.com/GenesisM8" target="_blank" rel="noopener noreferrer">GitHub</a>
                        </div>
                    </div>
                    <div className='developer'>
                        <img src="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/sandwich.png"/>
                        <div>
                            <h3>Jonathan Tabiendo</h3>
                            <a href="https://github.com/jontabiendo" target="_blank" rel="noopener noreferrer">GitHub</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}


export default Footer;
