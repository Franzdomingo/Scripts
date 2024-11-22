import os
import shutil

# Base directory
base_dir = r"G:\My Drive\Second Brain\ecommerce-app"

# Directory structure
directories = [
    "public/images/",
    "src/components/layout/",
    "src/components/ui/",
    "src/components/cart/",
    "src/components/product/",
    "src/components/admin/",
    "src/pages/products/",
    "src/pages/account/",
    "src/pages/admin/",
    "src/pages/auth/",
    "src/styles/",
    "src/utils/",
    "src/api/auth/",
    "src/api/products/",
    "src/api/orders/",
    "src/api/users/",
    "src/middleware/",
    "src/database/models/",
]

# Files to create with .md extension
files = [
    "public/favicon.ico.md",
    "src/components/layout/Header.tsx.md",
    "src/components/layout/Footer.tsx.md",
    "src/components/layout/Navbar.tsx.md",
    "src/components/ui/Button.tsx.md",
    "src/components/ui/Modal.tsx.md",
    "src/components/ui/Input.tsx.md",
    "src/components/ui/Loader.tsx.md",
    "src/components/cart/CartSummary.tsx.md",
    "src/components/cart/CartItem.tsx.md",
    "src/components/cart/CartIcon.tsx.md",
    "src/components/product/ProductCard.tsx.md",
    "src/components/product/ProductList.tsx.md",
    "src/components/product/ProductDetails.tsx.md",
    "src/components/admin/ProductTable.tsx.md",
    "src/components/admin/OrderTable.tsx.md",
    "src/components/admin/DashboardCard.tsx.md",
    "src/pages/index.tsx.md",
    "src/pages/products/index.tsx.md",
    "src/pages/products/[id].tsx.md",
    "src/pages/cart.tsx.md",
    "src/pages/checkout.tsx.md",
    "src/pages/account/index.tsx.md",
    "src/pages/account/orders.tsx.md",
    "src/pages/account/settings.tsx.md",
    "src/pages/admin/index.tsx.md",
    "src/pages/admin/products.tsx.md",
    "src/pages/admin/orders.tsx.md",
    "src/pages/auth/login.tsx.md",
    "src/pages/auth/register.tsx.md",
    "src/pages/404.tsx.md",
    "src/styles/globals.css.md",
    "src/styles/tailwind.css.md",
    "src/utils/api.ts.md",
    "src/utils/formatPrice.ts.md",
    "src/utils/validateInput.ts.md",
    "src/api/auth/login.ts.md",
    "src/api/auth/register.ts.md",
    "src/api/products/create.ts.md",
    "src/api/products/update.ts.md",
    "src/api/products/delete.ts.md",
    "src/api/orders/create.ts.md",
    "src/api/orders/get.ts.md",
    "src/api/orders/update.ts.md",
    "src/api/users/getUser.ts.md",
    "src/api/users/updateUser.ts.md",
    "src/middleware/authMiddleware.ts.md",
    "src/database/connect.ts.md",
    "src/database/models/User.ts.md",
    "src/database/models/Product.ts.md",
    "src/database/models/Order.ts.md",
    ".env.md",
    "next.config.js.md",
    "tailwind.config.js.md",
    "tsconfig.json.md",
    "package.json.md",
    "README.md",
]

# Delete previous structure
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
    print(f"Deleted previous structure at {base_dir}.")

# Recreate directories
for directory in directories:
    path = os.path.join(base_dir, directory)
    os.makedirs(path, exist_ok=True)

# Recreate files with .md extension
for file in files:
    path = os.path.join(base_dir, file)
    # Ensure the directory exists for nested files
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a"):
        pass

print(f"Directory and file structure recreated successfully with .md extensions at {base_dir}.")
