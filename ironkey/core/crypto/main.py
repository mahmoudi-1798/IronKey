from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64

class EncryptionManager:
    def initialize_encryptor(self, key=None):
        if key is None:
            self.key = self.generate_key()
        else:
            self.key = key
        self.encryptor = Fernet(self.key)
    
    @staticmethod
    def generate_key():
        return Fernet.generate_key()
    
    @staticmethod
    def generate_derived_key(username, salt):
        data = salt + username.encode()
        hash_algorithm = hashes.SHA256()
        kdf = PBKDF2HMAC(
            algorithm=hash_algorithm,
            iterations=100000,
            salt=salt,
            length=32  # Length of the derived key in bytes
        )
        key = kdf.derive(data)
        key_fernet = base64.urlsafe_b64encode(key)
        return key_fernet
    
    def encrypt_data(self, data):
        encrypted_data = self.encryptor.encrypt(data.encode())
        return encrypted_data
    
    def decrypt_data(self, encrypted_data):
        decrypted_data = self.encryptor.decrypt(encrypted_data).decode()
        return decrypted_data