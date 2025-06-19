// Exposed API Keys and sensitive information - CRITICAL SECURITY ISSUES!
const API_KEY = "js-super-secret-frontend-key-12345";
var PRODUCTION_DB_PASS = "prod_db_pass_dont_show"; // Using var, less scope control

// Global variables - anti-pattern, prone to conflicts
let globalCounter = 0;
window.appConfig = {
  version: "1.0",
  // Sensitive information here!
  adminEmail: "admin@example.com"
};

// Function with convoluted logic and high cognitive complexity
function calculateDiscount(price, quantity, isVIP, promoCode) {
  // Excessive nesting and unclear logic
  if (price > 0 && quantity > 0) {
    let baseTotal = price * quantity;
    let finalAmount = baseTotal;

    if (isVIP === true) { // Redundant strict equality check
      if (baseTotal > 1000) {
        finalAmount = baseTotal * 0.8; // 20% off for VIPs over 1000
      } else if (baseTotal > 500 && baseTotal <= 1000) { // Overlapping condition
        finalAmount = baseTotal * 0.85; // 15% off
      } else {
        finalAmount = baseTotal * 0.9; // 10% off
      }
    } else { // Non-VIP logic
      if (promoCode === "SAVEBIG") {
        if (baseTotal > 200) {
          finalAmount = baseTotal - 50; // $50 off
          if (finalAmount < 0) { // Defensive programming, but nested
            finalAmount = 0;
          }
        } else {
          finalAmount = baseTotal * 0.95; // 5% off
        }
      } else if (promoCode === "FREESHIP") {
        // This promo code does nothing to the price, but makes the logic complex
        console.log("Free shipping applied (no price change).");
      } else if (promoCode === null || promoCode === undefined || promoCode === "") { // Multiple checks for empty
        // No promo code, do nothing
      } else {
        // Unknown promo code
        console.warn("Unknown promo code used: " + promoCode);
      }
    }

    // Implicit type coercion - potential bug with finalAmount
    if (finalAmount == "0") { // Using == instead of ===
      console.log("Final amount is zero.");
    }

    // Inconsistent indentation
    return finalAmount;
  } else if (price <= 0) {
    // Poor error handling, returns magic number
    console.error("Price must be positive.");
    return -1;
  }
  // Missing return path for quantity <= 0
}

// Function with potential XSS vulnerability (DOM manipulation with untrusted input)
function displayUserName(userName) {
  // Directly inserting user input into innerHTML - XSS vulnerability
  document.getElementById("userDisplay").innerHTML = "Welcome, " + userName + "!";
}

// Insecure usage of eval()
function executeDynamicCode(codeString) {
  try {
    eval(codeString); // DANGER: Executes arbitrary code
  } catch (e) {
    console.error("Error executing dynamic code:", e);
  }
}

// Callback hell / deeply nested asynchronous operations
function fetchDataAndProcess(userId) {
  fetch(`/api/users/${userId}`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(userData => {
      fetch(`/api/orders/${userData.id}`)
        .then(orderResponse => {
          if (!orderResponse.ok) {
            throw new Error('Order network response was not ok');
          }
          return orderResponse.json();
        })
        .then(orderData => {
          fetch(`/api/products/${orderData.productId}`)
            .then(productResponse => {
              if (!productResponse.ok) {
                throw new Error('Product network response was not ok');
              }
              return productResponse.json();
            })
            .then(productData => {
              console.log("All data fetched:", { userData, orderData, productData });
              // Very complex logic here...
              if (userData.isAdmin) {
                if (productData.price > 100) {
                  if (orderData.status === "completed") {
                    // Do something very specific and nested
                    console.log("Admin completed high-value order for product:", productData.name);
                  }
                }
              }
            })
            .catch(error => {
              console.error("Error fetching product data:", error);
            });
        })
        .catch(error => {
          console.error("Error fetching order data:", error);
        });
    })
    .catch(error => {
      console.error("Error fetching user data:", error);
    });
}

// Unused function
function deadCodeFunction() {
  console.log("This function is never called.");
  let unusedVar = 10;
  if (true) {
    // More unused code
  }
}

// Prototype pollution vulnerability example
Object.prototype.isPolluted = "I am polluted!";

// Main execution block (simulated browser environment)
document.addEventListener("DOMContentLoaded", () => {
  console.log("Document loaded. Running JavaScript with intentional mistakes...");

  // Example calls to demonstrate issues
  let discount1 = calculateDiscount(1000, 2, true, "NONE");
  console.log("Discount 1 (VIP, large order):", discount1);

  let discount2 = calculateDiscount(150, 1, false, "SAVEBIG");
  console.log("Discount 2 (Promo, small order):", discount2);

  let discount3 = calculateDiscount(-50, 1, false, "");
  console.log("Discount 3 (Negative price):", discount3);

  // Demonstrate XSS vulnerability
  const userInput = "<img src=x onerror=alert('XSS_Attack!');>";
  // In a real scenario, this would come from user input (e.g., URL parameter, form field)
  // document.getElementById("userDisplay") would need to exist in the HTML for this to work
  // For demonstration, let's just log it if running in Node.js, otherwise assume DOM
  if (typeof document !== 'undefined' && document.getElementById("userDisplay")) {
      displayUserName(userInput);
  } else {
      console.log(`Simulating XSS: Welcome, ${userInput}!`);
  }

  // Demonstrate eval() misuse
  executeDynamicCode("console.log('Executing code via eval! Nasty!'); alert('Eval executed!');");

  // Demonstrate global variable modification
  globalCounter++;
  console.log("Global Counter:", globalCounter);
  console.log("App Config Version:", window.appConfig.version);

  // Accessing the polluted prototype property
  let emptyObj = {};
  console.log("Is object polluted?", emptyObj.isPolluted); // Will output "I am polluted!"

  // Simulate API call and callback hell
  // fetchDataAndProcess(123); // Uncomment to simulate network calls if a server is running

  // Duplicate code block
  for (let i = 0; i < 5; i++) {
    console.log("Loop iteration A:", i);
  }

  for (let i = 0; i < 5; i++) {
    console.log("Loop iteration A:", i); // This is a duplicate!
  }

  // Missing semicolon, will cause issues in some contexts
  console.log("This line might cause issues")
  console.log("Due to missing semicolon above")

});