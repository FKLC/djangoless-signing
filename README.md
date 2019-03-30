# Djangoless Signing
Same Django signing API but without Django

## Why Djangoless, why you can call it something else?
Because I only removed the `django.conf.settings` part and made really small changes on it, I don't think I should call it as my project. So instead of renaming it to something like 'HMAC/SHA1 Signer' I think it is much more ethic to keep using this name

## I did nothing
Since this library only a modified version of `django.core.signing` all of the kudos goes to Django engineers.

## Documentation
There is no such a thing since the library API is same as Django's so [click here for official Django Documentation.](https://docs.djangoproject.com/en/dev/topics/signing/)

__BUT__ if you are wondering what should I import here is the list of it:
- `from django.core.signing import Signer` = `from djangoless_signing import Signer`
- `from django.core.signing import TimestampSigner` = `from djangoless_signing import TimestampSigner`
- `from django.core import signing` = `import djangoless_signing`
