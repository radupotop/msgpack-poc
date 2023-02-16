from datetime import datetime
import msgpack
from uuid import UUID
import json

def encoder(obj):
    """Encoder for custom data types"""
    if isinstance(obj, datetime):
        return {'@dt': True, '#': obj.timestamp()}  # unix timestamp, float
    elif isinstance(obj, UUID):
        return {'@uid': True, '#': obj.bytes}  # bytes
    return obj

def decoder(obj):
    if '@dt' in obj:
        obj = datetime.fromtimestamp(obj['#'])
    elif '@uid' in obj:
        obj = UUID(bytes=obj['#'])
    return obj

payload_native = {'webhookEventUid': UUID('cbd5d458-ffa9-49d3-9d5a-0007bb913765'),
 'webhookType': 'FEED_ITEM',
 'eventTimestamp': datetime(2023, 2, 16, 18, 13, 56, 429186),
 'accountHolderUid': UUID('c2aa79e7-6749-4ba2-83fa-36c69699f266'),
 'content': {'feedItemUid': UUID('59d15af8-e715-4772-b3cd-9db46a37ed28'),
  'categoryUid': UUID('8a989356-b5fd-499b-b2fe-80e2cc8425fb'),
  'accountUid': UUID('3e807846-3dc4-4281-804c-acf211b6e37d'),
  'amount': {'currency': 'GBP', 'minorUnits': 5600},
  'sourceAmount': {'currency': 'GBP', 'minorUnits': 5600},
  'direction': 'IN',
  'updatedAt': datetime(2023, 2, 16, 18, 14, 53, 853960),
  'transactionTime': datetime(2023, 2, 15, 18, 14, 53, 853960),
  'settlementTime': datetime(2023, 2, 16, 18, 14, 53, 853960),
  'source': 'FASTER_PAYMENTS_IN',
  'status': 'SETTLED',
  'counterPartyType': 'SENDER',
  'counterPartyName': 'Faster payment',
  'counterPartySubEntityName': '',
  'counterPartySubEntityIdentifier': '600522',
  'counterPartySubEntitySubIdentifier': '20026250',
  'reference': 'test123',
  'country': 'GB',
  'spendingCategory': 'INCOME',
  'hasAttachment': False,
  'receiptPresent': False}}

payload_str = {'webhookEventUid': 'cbd5d458-ffa9-49d3-9d5a-0007bb913765',
 'webhookType': 'FEED_ITEM',
 'eventTimestamp': '2023-02-15T16:49:35.626Z',
 'accountHolderUid': 'c2aa79e7-6749-4ba2-83fa-36c69699f266',
 'content': {'feedItemUid': '59d15af8-e715-4772-b3cd-9db46a37ed28',
  'categoryUid': '8a989356-b5fd-499b-b2fe-80e2cc8425fb',
  'accountUid': '3e807846-3dc4-4281-804c-acf211b6e37d',
  'amount': {'currency': 'GBP', 'minorUnits': 5600},
  'sourceAmount': {'currency': 'GBP', 'minorUnits': 5600},
  'direction': 'IN',
  'updatedAt': '2023-02-15T16:49:35.594Z',
  'transactionTime': '2023-02-15T16:49:35.000Z',
  'settlementTime': '2023-02-15T16:49:35.000Z',
  'source': 'FASTER_PAYMENTS_IN',
  'status': 'SETTLED',
  'counterPartyType': 'SENDER',
  'counterPartyName': 'Faster payment',
  'counterPartySubEntityName': '',
  'counterPartySubEntityIdentifier': '600522',
  'counterPartySubEntitySubIdentifier': '20026250',
  'reference': 'test123',
  'country': 'GB',
  'spendingCategory': 'INCOME',
  'hasAttachment': False,
  'receiptPresent': False}}


packed_native = msgpack.packb(payload_native, default=encoder, use_bin_type=True)
packed_str = msgpack.packb(payload_str, default=encoder, use_bin_type=True)

unpacked_native = msgpack.unpackb(packed_native, object_hook=decoder, raw=False)

print(packed_native)
print('----')
print(packed_str)
print('----')
print(unpacked_native)
print('----')

print('packed_native', len(packed_native))
print('packed_str   ', len(packed_str))
print('json         ', len(json.dumps(payload_str)))
