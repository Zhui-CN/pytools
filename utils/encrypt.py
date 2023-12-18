# -*- coding: utf-8 -*-

import hmac
import base64
from .encode import encode
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, DES, DES3, ARC4, PKCS1_v1_5
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import MD5, SHA1, SHA224, SHA256, SHA384, SHA512


class MDAEncrypt:
    mda_map = {
        "MD5": MD5,
        "SHA1": SHA1,
        "SHA224": SHA224,
        "SHA256": SHA256,
        "SHA384": SHA384,
        "SHA512": SHA512,
        "HMAC": hmac,
    }

    @classmethod
    def encrypt(cls, mda_type, text, salt=None, b64=False):
        text = encode(text)
        if "HMAC" in mda_type:
            m = hmac.new(encode(salt), text, mda_type.split("-")[1])
            if b64:
                cipher_text = base64.b64encode(m.digest()).decode()
            else:
                cipher_text = m.hexdigest()
            return cipher_text
        else:
            return cls.mda_map[mda_type].new(text).hexdigest()


class SymmetricEncryption:
    symmetric_map = {
        "AES": AES,
        "DES": DES,
        "3DES": DES3,
        "RC4": ARC4
    }

    def __init__(self, symmetric_type, mode, key, length, iv=None, fill="pkcs7", b64=False):
        package = self.symmetric_map[symmetric_type]
        key = encode(key)
        try:
            mode = getattr(package, f"MODE_{mode}")
        except:
            mode = None
        iv = encode(iv) if iv else None
        self.length = length
        self.b64 = b64
        self.fill = fill
        self.key = key
        if iv and mode:
            self.encryption = package.new(key, mode, iv)
        elif mode:
            self.encryption = package.new(key, mode)
        else:
            self.encryption = package.new(key)

    def rc4_encrypt(self, plain_text):
        return base64.b64encode(self.encryption.encrypt(encode(plain_text))).decode()

    def rc4_decrypt(self, cipher_text):
        return self.encryption.decrypt(base64.b64decode(encode(cipher_text))).decode()

    def encrypt(self, plain_text):
        if isinstance(self.encryption, ARC4.ARC4Cipher):
            cipher_text = self.rc4_encrypt(plain_text)
        else:
            plain_text = pad(encode(plain_text), self.length, self.fill)
            cipher = self.encryption.encrypt(plain_text)
            if self.b64:
                cipher_text = base64.b64encode(cipher).decode().strip()
            else:
                cipher_text = cipher.hex()
        return cipher_text

    def decrypt(self, cipher_text):
        if isinstance(self.encryption, ARC4.ARC4Cipher):
            plain_text = self.rc4_decrypt(cipher_text)
        else:
            if self.b64:
                cipher_text = base64.b64decode(encode(cipher_text))
            else:
                cipher_text = bytes.fromhex(cipher_text)
            plain_text = self.encryption.decrypt(cipher_text)
            plain_text = unpad(plain_text, self.length, self.fill).decode().strip()
        return plain_text


class RSAEncrypt:
    """
    1024位的证书，加密时最大支持117个字节，解密时为128；
    2048位的证书，加密时最大支持245个字节，解密时为256。
    加密大文件时需要先用AES或者DES加密，再用RSA加密密钥，详细见文档
    文档:https://stuvel.eu/files/python-rsa-doc/usage.html#generating-keys
    """
    @classmethod
    def generate_key_pairs(cls, length=1024):
        k = RSA.generate(length)
        public_key = k.public_key().export_key()
        private_key = k.export_key()
        return public_key, private_key

    @staticmethod
    def encrypt(public_key, text):
        text = encode(text)
        if "BEGIN PUBLIC KEY" not in public_key:
            public_key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
        rsa_key = RSA.importKey(public_key)
        # return base64.b64encode(PKCS1_OAEP.new(rsa_key).encrypt(encode(text))).decode()
        return base64.b64encode(PKCS1_v1_5.new(rsa_key).encrypt(encode(text))).decode().strip()

    @staticmethod
    def decrypt(private_key, text):
        if "BEGIN RSA PRIVATE KEY" not in private_key:
            private_key = '-----BEGIN RSA PRIVATE KEY-----\n' + private_key + '\n-----END RSA PRIVATE KEY-----'
        rsa_key = RSA.importKey(private_key)
        # return PKCS1_OAEP.new(rsa_key).decrypt(base64.b64decode(encode(text))).decode()
        return PKCS1_v1_5.new(rsa_key).decrypt(base64.b64decode(encode(text)), None).decode()


class RailFenceCipher:
    """栏数有BUG"""

    def __init__(self, fence_num, space=""):
        self.fence_num = int(fence_num)
        self.space = space.strip() or "!@!"

    def encrypt(self, plain_text):
        plain_text = plain_text.replace(" ", self.space)
        plain_ls = list(plain_text)
        plain_ls = [plain_ls[i:i + self.fence_num] for i in range(0, len(plain_ls), self.fence_num)]
        fence_ls = [[] for _ in range(self.fence_num)]
        for p_ls in plain_ls:
            for i, v in enumerate(p_ls):
                fence_ls[i].append(v)
        cipher_text = ""
        for ls in fence_ls:
            cipher_text += "".join(ls)
        return cipher_text

    def decrypt(self, cipher_text: str):
        cipher_ls = [[] for _ in range(0, len(cipher_text), self.fence_num)]
        index = 0
        for i, t in enumerate(cipher_text):
            if i % len(cipher_ls) != 0:
                index += 1
            else:
                index = 0
            cipher_ls[index].append(t)
        plain_text = ""
        for ls in cipher_ls:
            plain_text += "".join(ls)
        plain_text = plain_text.replace(self.space, " ")
        return plain_text
