import { useHistory } from 'react-router-dom/cjs/react-router-dom.min'
import './CheckoutPage.css'

export default function CheckOutModal() {
    const history = useHistory()
    setTimeout(history.push, 3000, '/restaurants')
    return (
        <div id='successful-box'>
            <div>
                Checkout Successful!

                Returning you to main page...
            </div>
        </div>
    )
}
