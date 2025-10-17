#!/usr/bin/env python3
"""
Setup script for Infinity Blog
This script helps set up the environment and initial configuration.
"""

import os
import secrets
import shutil

def generate_secret_key():
    """Generate a secure secret key."""
    return secrets.token_urlsafe(32)

def setup_environment():
    """Set up the .env file with secure defaults."""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("✓ Created .env file from template")
            
            # Replace the default secret key with a secure one
            with open('.env', 'r') as f:
                content = f.read()
            
            secure_key = generate_secret_key()
            content = content.replace('your-secret-key-here', secure_key)
            
            with open('.env', 'w') as f:
                f.write(content)
            
            print("✓ Generated secure secret key")
            print("✓ Environment setup complete!")
            print("\nNext steps:")
            print("1. Edit .env file to customize admin user settings")
            print("2. Run: python main.py")
        else:
            print("❌ .env.example file not found")
    else:
        print("✓ .env file already exists")

def create_instance_dir():
    """Create instance directory for database."""
    if not os.path.exists('instance'):
        os.makedirs('instance')
        print("✓ Created instance directory")
    else:
        print("✓ Instance directory already exists")

if __name__ == "__main__":
    print("Setting up Infinity Blog...")
    print("=" * 40)
    
    create_instance_dir()
    setup_environment()
    
    print("\n" + "=" * 40)
    print("Setup complete! You can now run the application.")