<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Payment</title>
<link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
<link rel="stylesheet" href="{{url_for('static',filename='payment.css')}}">
</head>
<body>
    <div class="backtohome">
        <h2 style="text-transform: uppercase; border: 3px solid #fff; background-color: #31572c; ">
            <span>
                <a href="/home1" target="_parent" style="padding-right: 520px;">
                    <i class='bx bx-chevrons-left' ></i>Back to home
                </a>
            </span>
            <span>Checkout</span>
        </h2>
    </div>
    
    <div class="row">
        <div class="col-75">
            <div class="container">
                <form action="/payment" method="post" id="checkout-form" onsubmit="return validateForm()">
                    <div class="row">
                        <div class="col-50">
                            <h3 >CONTACT INFORMATION-</h3>
                            <label for="fname"><i class='bx bx-user'></i>Full Name</label>
                            <input type="text" id="fname" name="fname" placeholder="Enter your fullname" required>
                            <label for="adr"><i class='bx bx-location-plus'></i>Address</label>
                            <input type="text" id="adr" name="address" placeholder="Enter your address" required>
                            <label for="city"><i class='bx bx-buildings' ></i>City</label>
                            <input type="text" id="city" name="city" placeholder="Enter your city" required>
                            <div class="row">
                                <div class="col-50">
                                    <label for="Phone"><i class='bx bx-phone' ></i>Phone no</label>
                                    <input type="tel" id="Phone" name="phone" placeholder="Enter your Phone no" style="height: 41px; border-radius: 4px;" required>
                                </div>
                                <div class="col-50">
                                    <label for="zip">Pincode</label>
                                    <input type="text" id="zip" name="pincode" placeholder="Pincode" required>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-50">
                            <h3>PAYMENT METHODS-</h3>
                            <label for="payment_method">Payment Method</label>
                            <select id="payment_method" name="payment_method" required>
                                <option value="cash_on_delivery" >Cash on Delivery</option>
                                <option value="upi">UPI (COMING SOON)</option>
                            </select><br>
                        </div>
                       
                    </div>
                    <input type="submit" class="btn-submit" id="submit" value="SUBMIT">
                </form>
                <div class="popup" id="popup">
                    <img src="/static/tick.webp" alt="Tick">
                    <h4>Thank-you!</h4>
                    <p>Your order has been placed successfully.</p>
                    <button type="button" onclick="closepopup()">OK</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Include animation.js script -->
    
    <script>
        let popup = document.getElementById('popup');

        function openpopup() {
            popup.classList.add("open-popup");
        }

        function closepopup() {
            popup.classList.remove("open-popup");
            // Redirect to home page after closing the popup
            window.location.href = "/";
        }

        function validateForm() {
            var inputs = document.getElementsByTagName('input');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].hasAttribute('required') && !inputs[i].value) {
                    alert('Please fill in all required fields.');
                    return false;
                }
            }
            openpopup(); // Open popup if form is valid
            return false; // Prevent default form submission
        }
    </script>
</body>
</html>
