UNREAD_ENTRIES = 'unread'
READ_ENTRIES = 'read'

FILTER_CONSTANTS = {
    UNREAD_ENTRIES: {'read_dt__isnull':True},
    READ_ENTRIES: {'read_dt__isnull':False},
}