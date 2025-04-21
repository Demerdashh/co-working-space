<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  

</head>
<body>

  <h1>Coworking Space Management System</h1>

  <p>
    <span class="badge license">License: Open</span>
<br>
    <span class="badge python">Python 3.x</span>
    <br>
    <span class="badge dependencies">Dependencies: ttkthemes</span>
  </p>

  <h2>Overview</h2>
  <p>
    The <strong>Coworking Space Management System</strong> is a desktop application designed to assist administrators in managing coworking spaces efficiently. This Python-based application uses the <code>tkinter</code> library for the graphical user interface (GUI) and provides tools for handling customer check-ins, room bookings, item purchases, and billing calculations.
  </p>
  <p>Key features include:</p>
  <ul>
    <li><strong>Customer Check-In</strong>: Administrators can register customers and assign them to different room types.</li>
    <li><strong>Dynamic Billing</strong>: Automatically calculates charges based on room type, duration, and additional purchases.</li>
    <li><strong>Add Purchases</strong>: Allows administrators to add items like coffee, tea, or snacks to a customer's bill.</li>
    <li><strong>Checkout Process</strong>: Generates a detailed bill with breakdowns of charges when a customer checks out.</li>
    <li><strong>Real-Time Updates</strong>: Displays live updates for session durations and total charges.</li>
  </ul>
  <p>This system is ideal for small to medium-sized coworking spaces looking to streamline their operations.</p>

  <h2>Table of Contents</h2>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>

  <h2 id="features">Features</h2>
  <h3>For Administrators:</h3>
  <ul>
    <li><strong>Customer Management</strong>: Add and manage customer sessions with ease.</li>
    <li><strong>Room Booking</strong>: Assign customers to different room types (Standard, Premium, VIP, Private).</li>
    <li><strong>Billing System</strong>: Dynamically calculate charges based on room type, duration, and additional purchases.</li>
    <li><strong>Item Purchases</strong>: Add items like coffee, tea, water, or snacks to a customer's bill.</li>
    <li><strong>Session Details</strong>: View real-time details of active customer sessions, including duration and total charges.</li>
    <li><strong>Checkout Process</strong>: Generate detailed bills with breakdowns of workspace charges and purchases.</li>
  </ul>

  <h2 id="installation">Installation</h2>
  <p>To set up the project locally, follow these steps:</p>
  <ol>
    <li><strong>Prerequisites</strong>:
      <ul>
        <li>Ensure you have Python 3.x installed on your system. You can download it from <a href="https://www.python.org/downloads/">python.org</a>.</li>
        <li>Install the required dependencies by running:
          <pre>pip install ttkthemes</pre>
        </li>
      </ul>
    </li>
    <li><strong>Clone the Repository</strong>:
      <pre>
git clone https://github.com/Demerdashh/working-space.git
cd working-space
      </pre>
    </li>
    <li><strong>Run the Application</strong>:
      Execute the main script to launch the application:
      <pre>python workSpace.py</pre>
    </li>
    <li><strong>Customize (Optional)</strong>:
      <ul>
        <li>Modify the <code>ROOM_PRICES</code> and <code>ITEM_PRICES</code> dictionaries in the code to match your coworking space's pricing structure.</li>
        <li>Replace the <code>path\\letter-m.ico</code> file with your own icon if desired.</li>
      </ul>
    </li>
  </ol>

  <h2 id="usage">Usage</h2>
  <h3>Customer Management:</h3>
  <ol>
    <li>Enter the customer's name in the "Customer Name" field.</li>
    <li>Select the room type from the dropdown menu (e.g., Standard, Premium, VIP, Private).</li>
    <li>Click the <strong>Check In</strong> button to register the customer.</li>
  </ol>
  <h3>Adding Purchases:</h3>
  <ol>
    <li>Select a customer from the list by double-clicking their name.</li>
    <li>Choose an item (e.g., Coffee, Tea, Water, Snacks) from the dropdown menu.</li>
    <li>Click the <strong>Add Item</strong> button to add the purchase to the customer's bill.</li>
  </ol>
  <h3>Checkout Process:</h3>
  <ol>
    <li>Select a customer from the list.</li>
    <li>Click the <strong>Checkout</strong> button to generate a detailed bill with the following information:
      <ul>
        <li>Customer name</li>
        <li>Room type and hourly rate</li>
        <li>Duration of stay</li>
        <li>Workspace charges</li>
        <li>List of purchased items</li>
        <li>Total charge</li>
      </ul>
    </li>
  </ol>
  <h3>Real-Time Updates:</h3>
  <p>Double-click on a customer's name in the list to view a detailed session window. The session window displays:</p>
  <ul>
    <li>Check-in time</li>
    <li>Current duration</li>
    <li>List of purchased items</li>
    <li>Total charges (updated in real-time)</li>
  </ul>

  <h2 id="technologies-used">Technologies Used</h2>
  <ul>
    <li><strong>Programming Language</strong>: Python 3.x</li>
    <li><strong>GUI Framework</strong>: <code>tkinter</code> and <code>ttkthemes</code></li>
    <li><strong>Data Structures</strong>: Dictionaries and lists for managing customer sessions and pricing.</li>
    <li><strong>Libraries</strong>:
      <ul>
        <li><code>datetime</code>: For calculating session durations.</li>
        <li><code>messagebox</code> and <code>ttk</code>: For interactive dialogs and styled widgets.</li>
      </ul>
    </li>
  </ul>

  <h2 id="contributing">Contributing</h2>
  <p>We welcome contributions from the community! To contribute:</p>
  <ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature/YourFeatureName</code>).</li>
    <li>Commit your changes (<code>git commit -m "Add YourFeatureName"</code>).</li>
    <li>Push to the branch (<code>git push origin feature/YourFeatureName</code>).</li>
    <li>Open a pull request.</li>
  </ol>
  <p>Please ensure your code adheres to Python best practices and includes appropriate documentation.</p>
</body>
</html>
