# Functions by Module

## .py

- `parsedate_tz(data)`
- `_parsedate_tz(data)`
- `parsedate(data)`
- `mktime_tz(data)`
- `quote(str)`
- `__init__(self, field)`
  - Docstring: Initialize a new instance.

        `field' is an unparsed address header field, containing
        one or more addresses.
- `gotonext(self)`
- `getaddrlist(self)`
- `getaddress(self)`
- `getrouteaddr(self)`
- `getaddrspec(self)`
- `getdomain(self)`
- `getquote(self)`
  - Docstring: Get a quote-delimited fragment from self's field.
- `getcomment(self)`
  - Docstring: Get a parenthesis-delimited fragment from self's field.
- `getdomainliteral(self)`
- `getphraselist(self)`
- `__init__(self, field)`
- `__len__(self)`
- `__add__(self, other)`
- `__iadd__(self, other)`
- `__sub__(self, other)`
- `__isub__(self, other)`
- `__getitem__(self, index)`

## _abc

- `create_module(self, spec)`
- `load_module(self, fullname)`
- `module_repr(self, module)`
  - Docstring: Return a module's repr.

        Used by the module type when the method does not raise
        NotImplementedError.

        This method is deprecated.

## _adapters

- `__new__(cls = None, orig = None)`
- `__init__(self, *args, **kwargs)`
- `__iter__(self = None)`
- `_repair_headers(self)`
- `redent(value)`
- `json(self)`
- `transform(key = None)`

## _bootstrap

- `_object_name(obj)`
- `_wrap(new, old)`
- `_new_module(name)`
- `__init__(self, name)`
- `has_deadlock(self)`
- `acquire(self)`
- `release(self)`
- `__repr__(self)`
- `__init__(self, name)`
- `acquire(self)`
- `release(self)`
- `__repr__(self)`
- `__init__(self, name)`
- `__enter__(self)`
- `__exit__(self, *args, **kwargs)`
- `_get_module_lock(name)`
- `_lock_unlock_module(name)`
- `_call_with_frames_removed(f, *args, **kwds)`
- `_verbose_message(message = None, *, verbosity, *args)`
- `_requires_builtin(fxn)`
- `_requires_builtin_wrapper(self = None, fullname = None)`
- `_requires_frozen(fxn)`
- `_requires_frozen_wrapper(self = None, fullname = None)`
- `_load_module_shim(self, fullname)`
- `_module_repr(module)`
- `__init__(self, name = None, loader = {
        'origin': None,
        'loader_state': None,
        'is_package': None }, *, origin, loader_state, is_package)`
- `__repr__(self)`
- `__eq__(self, other)`
- `cached(self)`
- `cached(self, cached)`
  - Docstring: The name of the module's parent.
- `parent(self)`
  - Docstring: The name of the module's parent.
- `has_location(self)`
- `has_location(self, value)`
- `spec_from_loader(name = None, loader = {
    'origin': None,
    'is_package': None }, *, origin, is_package)`
- `_init_module_attrs(spec = None, module = {
    'override': False }, *, override)`
- `module_from_spec(spec)`
- `_module_repr_from_spec(spec)`
- `_exec(spec, module)`
  - Docstring: Execute the spec's specified module in an existing module's namespace.
- `_load_backward_compatible(spec)`
- `_load_unlocked(spec)`
- `_load(spec)`
- `module_repr(module)`
- `create_module(spec)`
- `exec_module(module)`
- `get_code(cls, fullname)`
- `get_source(cls, fullname)`
- `is_package(cls, fullname)`
- `module_repr(m)`
- `create_module(spec)`
- `exec_module(module)`
- `load_module(cls, fullname)`
- `get_code(cls, fullname)`
- `get_source(cls, fullname)`
- `is_package(cls, fullname)`
- `__enter__(self)`
- `__exit__(self, exc_type, exc_value, exc_traceback)`
- `_resolve_name(name, package, level)`
- `_find_spec_legacy(finder, name, path)`
- `_sanity_check(name, package, level)`
- `_find_and_load_unlocked(name, import_)`
- `_find_and_load(name, import_)`
- `_handle_fromlist(module, fromlist = None, import_ = {
    'recursive': False }, *, recursive)`
- `_calc___package__(globals)`
- `_builtin_from_name(name)`
- `_setup(sys_module, _imp_module)`
- `_install(sys_module, _imp_module)`
- `_install_external_importers()`

## _collections

- `__missing__(self = None, key = None)`
- `freeze(self)`
- `Pair()`
- `parse(cls, text)`

## _compression

- `_check_not_closed(self)`
- `_check_can_read(self)`
- `_check_can_write(self)`
- `_check_can_seek(self)`
- `readable(self)`
- `close(self = None)`
- `seekable(self)`
- `readinto(self, b)`
- `readall(self)`
- `_rewind(self)`
- `tell(self)`

## _encoded_words

- `decode_q(encoded)`
- `__missing__(self, key)`
- `encode_q(bstring)`
- `len_q(bstring)`
- `decode_b(encoded)`
- `encode_b(bstring)`
- `len_b(bstring)`
- `decode(ew)`

## _functools

- `wrapper(self = None, *args, **kwargs)`
- `pass_none(func)`
  - Docstring: Wrap func so it's not called if its first param is None

    >>> print_text = pass_none(print)
    >>> print_text('text')
    text
    >>> print_text(None)
- `wrapper(param = None, *args, **kwargs)`

## _header_value_parser

- `quote_string(value)`
- `__init__(self = None, *args, **kw)`
- `__str__(self)`
- `__repr__(self = None)`
- `value(self)`
- `all_defects(self)`
- `startswith_fws(self)`
- `as_ew_allowed(self)`
- `comments(self)`
- `fold(self, *, policy)`
- `value(self)`
- `comments(self)`
- `content(self)`
- `quoted_value(self)`
- `stripped_value(self)`
- `__str__(self)`
- `value(self)`
- `__str__(self)`
- `quote(self, value)`
- `content(self)`
- `comments(self)`
- `addresses(self)`
- `mailboxes(self)`
- `all_mailboxes(self)`
- `display_name(self)`
- `mailboxes(self)`
- `all_mailboxes(self)`
- `mailboxes(self)`
- `all_mailboxes(self)`
- `mailboxes(self)`
- `all_mailboxes(self)`
- `mailboxes(self)`
- `all_mailboxes(self)`
- `display_name(self)`
- `display_name(self)`
- `local_part(self)`
- `domain(self)`
- `route(self)`
- `addr_spec(self)`
- `local_part(self)`
- `domain(self)`
- `route(self)`
- `addr_spec(self)`
- `domains(self)`
- `display_name(self)`
- `local_part(self)`
- `domain(self)`
- `route(self)`
- `addr_spec(self)`
- `display_name(self)`
- `domain(self = None)`
- `local_part(self)`
- `domain(self)`
- `value(self)`
- `addr_spec(self)`
- `display_name(self)`
- `value(self = None)`
- `value(self)`
- `local_part(self)`
- `domain(self = None)`
- `ip(self)`
- `section_number(self)`
- `param_value(self)`
- `stripped_value(self)`
- `stripped_value(self)`
- `params(self)`
- `__str__(self)`
- `params(self)`
- `fold(self, policy)`
- `__new__(cls = None, value = None, token_type = None)`
- `__repr__(self = None)`
- `pprint(self)`
- `all_defects(self)`
- `_pp(self = None, indent = None)`
- `pop_trailing_ws(self)`
- `comments(self)`
- `__getnewargs__(self)`
- `value(self)`
- `startswith_fws(self)`
- `value(self)`
- `startswith_fws(self)`
- `value(self)`
- `__str__(self)`
- `_validate_xtext(xtext)`
- `_get_ptext_to_endchars(value, endchars)`
- `get_fws(value)`
- `get_encoded_word(value)`
- `get_unstructured(value)`
- `get_qp_ctext(value)`
- `get_qcontent(value)`
- `get_atext(value)`
  - Docstring: atext = <matches _atext_matcher>

    We allow any non-ATOM_ENDS in atext, but add an InvalidATextDefect to
    the token's defects list if we find non-atext characters.
- `get_bare_quoted_string(value)`
- `get_comment(value)`
- `get_cfws(value)`
- `get_quoted_string(value)`
- `get_atom(value)`
- `get_dot_atom_text(value)`

## _meta

- `__len__(self = None)`
- `__contains__(self = None, item = None)`
- `__getitem__(self = None, key = None)`
- `__iter__(self = None)`
- `get_all(self = None, name = None, failobj = None)`
- `json(self = None)`
- `joinpath(self = None)`
- `__div__(self = None)`
- `parent(self = None)`
- `read_text(self = None)`

## _parseaddr

- `parsedate_tz(data)`
- `_parsedate_tz(data)`
- `parsedate(data)`
- `mktime_tz(data)`
- `quote(str)`
- `__init__(self, field)`
  - Docstring: Initialize a new instance.

        `field' is an unparsed address header field, containing
        one or more addresses.
- `gotonext(self)`
- `getaddrlist(self)`
- `getaddress(self)`
- `getrouteaddr(self)`
- `getaddrspec(self)`
- `getdomain(self)`
- `getquote(self)`
  - Docstring: Get a quote-delimited fragment from self's field.
- `getcomment(self)`
  - Docstring: Get a parenthesis-delimited fragment from self's field.
- `getdomainliteral(self)`
- `getphraselist(self)`
- `__init__(self, field)`
- `__len__(self)`
- `__add__(self, other)`
- `__iadd__(self, other)`
- `__sub__(self, other)`
- `__isub__(self, other)`
- `__getitem__(self, index)`

## _policybase

- `__init__(self = None, **kw)`
- `__repr__(self)`
- `clone(self, **kw)`
- `__setattr__(self, name, value)`
- `__add__(self, other)`
- `_append_doc(doc, added_doc)`
- `_extend_docstrings(cls)`
- `handle_defect(self, obj, defect)`
- `register_defect(self, obj, defect)`
- `header_max_count(self, name)`
- `header_source_parse(self, sourcelines)`
- `header_store_parse(self, name, value)`
- `header_fetch_parse(self, name, value)`
- `fold(self, name, value)`
- `fold_binary(self, name, value)`

## _py_abc

- `get_cache_token()`
- `__new__(mcls = None, name = None, bases = None, namespace = None, **kwargs)`
- `register(cls, subclass)`
- `_abc_registry_clear(cls)`
- `_abc_caches_clear(cls)`
- `__instancecheck__(cls, instance)`
- `__subclasscheck__(cls, subclass)`

## _strptime

- `_getlang()`
- `__init__(self)`
- `__calc_weekday(self)`
- `__calc_month(self)`
- `__calc_am_pm(self)`
- `__calc_date_time(self)`
- `__calc_timezone(self)`
- `__init__(self = None, locale_time = None)`
- `__seqToRE(self, to_convert, directive)`
- `pattern(self, format)`
- `compile(self, format)`
- `_calc_julian_from_U_or_W(year, week_of_year, day_of_week, week_starts_Mon)`
- `_calc_julian_from_V(iso_year, iso_week, iso_weekday)`

## _text

- `__lt__(self, other)`
- `__gt__(self, other)`
- `__eq__(self, other)`
- `__ne__(self, other)`
- `__hash__(self)`
- `__contains__(self = None, other = None)`
- `in_(self, other)`
- `lower(self = None)`
- `index(self, sub)`

## _threading_local

- `__init__(self)`
- `get_dict(self)`
- `create_dict(self)`
- `local_deleted(_ = None, key = None)`
- `thread_deleted(_ = None, idt = None)`
- `_patch(self)`
- `__new__(cls, *args, **kw)`
- `__getattribute__(self, name)`
- `__setattr__(self, name, value)`
- `__delattr__(self, name)`

## base64

- `_bytes_from_decode_data(s)`
- `standard_b64encode(s)`
- `standard_b64decode(s)`
- `urlsafe_b64encode(s)`
- `urlsafe_b64decode(s)`
- `_b32encode(alphabet, s)`
- `b32encode(s)`
- `b32hexencode(s)`
- `b16encode(s)`
- `a85encode(b = None, *, foldspaces, wrapcol, pad, adobe)`
- `a85decode(b = None, *, foldspaces, adobe, ignorechars)`
- `b85decode(b)`
- `encode(input, output)`
- `decode(input, output)`
- `_input_type_check(s)`
- `encodebytes(s)`
- `decodebytes(s)`
- `main()`
- `test()`

## base64mime

- `header_length(bytearray)`
- `decode(string)`

## bz2

- `close(self)`
- `closed(self)`
- `fileno(self)`
- `seekable(self)`
- `readable(self)`
- `writable(self)`
- `readinto(self, b)`
- `write(self, data)`
- `writelines(self, seq)`
- `tell(self)`
- `decompress(data)`

## calendar

- `__init__(self, month)`
- `__str__(self)`
- `__init__(self, weekday)`
- `__str__(self)`
- `__init__(self, format)`
- `__getitem__(self, i)`
- `__len__(self)`
- `__init__(self, format)`
- `__getitem__(self, i)`
- `__len__(self)`
- `isleap(year)`
- `leapdays(y1, y2)`
- `weekday(year, month, day)`
- `monthrange(year, month)`
- `_monthlen(year, month)`
- `_prevmonth(year, month)`
- `_nextmonth(year, month)`
- `getfirstweekday(self)`
- `setfirstweekday(self, firstweekday)`
- `iterweekdays(self)`
- `itermonthdates(self, year, month)`
- `itermonthdays(self, year, month)`
- `itermonthdays2(self, year, month)`
- `itermonthdays3(self, year, month)`
- `itermonthdays4(self, year, month)`
- `monthdatescalendar(self, year, month)`
  - Docstring: Return a matrix (list of lists) representing a month's calendar.
        Each row represents a week; week entries are datetime.date values.
- `monthdays2calendar(self, year, month)`
- `monthdayscalendar(self, year, month)`
  - Docstring: Return a matrix representing a month's calendar.
        Each row represents a week; days outside this month are zero.
- `prweek(self, theweek, width)`
- `formatday(self, day, weekday, width)`
- `formatweek(self, theweek, width)`
- `formatweekday(self, day, width)`
- `formatweekheader(self, width)`
- `formatday(self, day, weekday)`
- `formatweek(self, theweek)`
- `formatweekday(self, day)`
- `formatweekheader(self)`
- `__init__(self, locale)`
- `__enter__(self)`
- `__exit__(self, *args)`
- `formatweekday(self = None, day = None, width = None)`
- `formatmonthname(self = None, theyear = None, themonth = None, width = None, withyear = None)`
- `formatweekday(self = None, day = None)`
- `formatmonthname(self = None, theyear = None, themonth = None, withyear = None)`
- `setfirstweekday(firstweekday)`
- `timegm(tuple)`
- `main(args)`

## contentmanager

- `__init__(self)`
- `add_get_handler(self, key, handler)`
- `get_content(self, msg, *args, **kw)`
- `add_set_handler(self, typekey, handler)`
- `set_content(self, msg, obj, *args, **kw)`
- `_find_set_handler(self, msg, obj)`
- `get_non_text_content(msg)`
- `get_message_content(msg)`
- `get_and_fixup_unknown_message_content(msg)`
- `_prepare_set(msg, maintype, subtype, headers)`
- `_finalize_set(msg, disposition, filename, cid, params)`
- `_encode_base64(data, max_line_length)`
- `_encode_text(string, charset, cte, policy)`
- `embedded_body(lines = None)`
- `normal_body(lines)`

## contextlib

- `__enter__(self)`
- `__exit__(self, exc_type, exc_value, traceback)`
- `__subclasshook__(cls, C)`
- `__subclasshook__(cls, C)`
- `_recreate_cm(self)`
- `__call__(self, func)`
- `inner(*args, **kwds)`
- `_recreate_cm(self)`
- `__call__(self, func)`
- `__init__(self, func, args, kwds)`
- `_recreate_cm(self)`
- `__enter__(self)`
- `__exit__(self, typ, value, traceback)`
- `contextmanager(func)`
- `some_generator(<arguments>)`
- `helper(*args, **kwds)`
- `asynccontextmanager(func)`
- `helper(*args, **kwds)`
- `__init__(self, thing)`
- `__enter__(self)`
- `__exit__(self, *exc_info)`
- `__init__(self, thing)`
- `__init__(self, new_target)`
- `__enter__(self)`
- `__exit__(self, exctype, excinst, exctb)`
- `__init__(self, *exceptions)`
- `__enter__(self)`
- `__exit__(self, exctype, excinst, exctb)`
- `_create_exit_wrapper(cm, cm_exit)`
- `_create_cb_wrapper(callback, *args, **kwds)`
- `_exit_wrapper(exc_type = None, exc = None, tb = None)`
- `__init__(self)`
- `pop_all(self)`
- `push(self, exit)`
- `enter_context(self, cm)`
- `callback(self, callback, *args, **kwds)`
- `_push_cm_exit(self, cm, cm_exit)`
- `__enter__(self)`
- `__exit__(self, *exc_details)`
- `_fix_exception_context(new_exc = None, old_exc = None)`
- `close(self)`
- `_create_async_exit_wrapper(cm, cm_exit)`
- `_create_async_cb_wrapper(callback, *args, **kwds)`
- `push_async_exit(self, exit)`
- `push_async_callback(self, callback, *args, **kwds)`
- `_push_async_cm_exit(self, cm, cm_exit)`
- `_fix_exception_context(new_exc = None, old_exc = None)`
- `__enter__(self)`
- `__exit__(self, *excinfo)`

## csv

- `__init__(self)`
- `_validate(self)`
- `__iter__(self)`
- `fieldnames(self)`
- `fieldnames(self, value)`
- `__next__(self)`
- `writeheader(self)`
- `_dict_to_list(self, rowdict)`
- `writerow(self, rowdict)`
- `writerows(self, rowdicts)`

## dataclasses

- `__repr__(self)`
- `__init__(self, name)`
- `__repr__(self)`
- `_recursive_repr(user_function)`
- `wrapper(self = None)`
- `__init__(self, type)`
- `__repr__(self)`
- `__class_getitem__(cls, type)`
- `__init__(self, default, default_factory, init, repr, hash, compare, metadata, kw_only)`
- `__repr__(self)`
- `__set_name__(self, owner, name)`
- `__init__(self, init, repr, eq, order, unsafe_hash, frozen)`
- `__repr__(self)`
- `field(*, default, default_factory, init, repr, hash, compare, metadata, kw_only)`
- `_fields_in_init_order(fields)`
- `_tuple_str(obj_name, fields)`
- `_create_fn(name, args = None, body = {
    'globals': None,
    'locals': None,
    'return_type': MISSING }, *, globals, locals, return_type)`
- `_field_assign(frozen, name, value, self_name)`
- `_field_init(f, frozen, globals, self_name, slots)`
- `_init_param(f)`
- `_init_fn(fields, std_fields, kw_only_fields, frozen, has_post_init, self_name, globals, slots)`
- `_repr_fn(fields, globals)`
- `_frozen_get_del_attr(cls, fields, globals)`
- `_cmp_fn(name, op, self_tuple, other_tuple, globals)`
- `_hash_fn(fields, globals)`
- `_is_classvar(a_type, typing)`
- `_is_initvar(a_type, dataclasses)`
- `_is_kw_only(a_type, dataclasses)`
- `_is_type(annotation, cls, a_module, a_type, is_type_predicate)`
- `_get_field(cls, a_name, a_type, default_kw_only)`
- `_set_qualname(cls, value)`
- `_set_new_attribute(cls, name, value)`
- `_hash_set_none(cls, fields, globals)`
- `_hash_add(cls, fields, globals)`
- `_hash_exception(cls, fields, globals)`

## datetime

- `_cmp(x, y)`
- `_is_leap(year)`
- `_days_before_year(year)`
- `_days_in_month(year, month)`
- `_days_before_month(year, month)`
- `_ymd2ord(year, month, day)`

## dis

- `_try_compile(source, name)`
- `dis(x = None, *, file, depth)`
- `distb(tb = None, *, file)`
- `pretty_flags(flags)`
- `_get_code_object(x)`
- `code_info(x)`
- `_format_code_info(co)`
- `show_code(co = None, *, file)`
- `get_instructions(x = None, *, first_line)`
- `_get_const_info(const_index, const_list)`
- `_get_name_info(name_index, name_list)`
- `_disassemble_recursive(co = None, *, file, depth)`
- `_disassemble_str(source, **kwargs)`
- `_unpack_opargs(code)`
- `findlabels(code)`
- `findlinestarts(code)`
- `__init__(self = None, x = {
        'first_line': None,
        'current_offset': None }, *, first_line, current_offset)`
- `__iter__(self)`
- `__repr__(self)`
- `from_traceback(cls, tb)`
- `info(self)`
- `dis(self)`
- `_test()`

## errors

- `__init__(self = None, line = None)`
- `__init__(self = None, *args, **kw)`
- `__init__(self = None, non_printables = None)`
- `__str__(self)`

## feedparser

- `__init__(self)`
- `push_eof_matcher(self, pred)`
- `pop_eof_matcher(self)`
- `close(self)`
- `readline(self)`
- `unreadline(self, line)`
- `push(self, data)`
- `pushlines(self, lines)`
- `__iter__(self)`
- `__next__(self)`
- `_set_headersonly(self)`
- `feed(self, data)`
- `_call_parse(self)`
- `close(self)`
- `_new_message(self)`
- `_pop_message(self)`
- `_parsegen(self)`
- `_parse_headers(self, lines)`
- `feed(self = None, data = None)`

## fnmatch

- `fnmatch(name, pat)`
- `_compile_pattern(pat)`
- `filter(names, pat)`
- `fnmatchcase(name, pat)`
  - Docstring: Test whether FILENAME matches PATTERN, including case.

    This is a version of fnmatch() which doesn't case-normalize
    its arguments.
- `translate(pat)`

## fractions

- `__new__(cls = None, numerator = None, denominator = None, *, _normalize)`
- `from_float(cls, f)`
- `from_decimal(cls, dec)`
- `as_integer_ratio(self)`
- `numerator(a)`
- `denominator(a)`
- `__repr__(self)`
- `__str__(self)`
- `_operator_fallbacks(monomorphic_operator, fallback_operator)`
- `__add__(self, other)`
- `__radd__(self, other)`
- `forward(a = None, b = None)`
- `reverse(b = None, a = None)`
- `_add(a, b)`
- `_sub(a, b)`
- `_mul(a, b)`
- `_div(a, b)`
- `_floordiv(a, b)`
- `_divmod(a, b)`
- `_mod(a, b)`
- `__pow__(a, b)`
- `__rpow__(b, a)`
- `__pos__(a)`
- `__neg__(a)`
- `__abs__(a)`
- `__trunc__(a)`
- `__floor__(a)`
- `__ceil__(a)`
- `__hash__(self)`
- `__eq__(a, b)`
- `_richcmp(self, other, op)`
- `__lt__(a, b)`
- `__gt__(a, b)`
- `__le__(a, b)`
- `__ge__(a, b)`
- `__bool__(a)`
- `__reduce__(self)`
- `__copy__(self)`
- `__deepcopy__(self, memo)`

## generator

- `write(self, s)`
- `clone(self, fp)`
- `_new_buffer(self)`
- `_encode(self, s)`
- `_write_lines(self, lines)`
- `_write(self, msg)`
- `_dispatch(self, msg)`
- `_write_headers(self, msg)`
- `_handle_text(self, msg)`
- `_handle_multipart(self, msg)`
- `_handle_multipart_signed(self, msg)`
- `_handle_message_delivery_status(self, msg)`
- `_handle_message(self, msg)`
- `_compile_re(cls, s, flags)`
- `write(self, s)`
- `_new_buffer(self)`
- `_encode(self, s)`
- `_write_headers(self, msg)`
- `_handle_text(self = None, msg = None)`
- `_compile_re(cls, s, flags)`
- `_dispatch(self, msg)`

## gettext

- `_tokenize(plural)`
- `_error(value)`
- `_as_int(n)`
- `c2py(plural)`

## glob

- `glob(pathname = None, *, root_dir, dir_fd, recursive)`
- `iglob(pathname = None, *, root_dir, dir_fd, recursive)`
- `_iglob(pathname, root_dir, dir_fd, recursive, dironly)`
- `_glob1(dirname, pattern, dir_fd, dironly)`
- `_glob0(dirname, basename, dir_fd, dironly)`
- `glob0(dirname, pattern)`
- `glob1(dirname, pattern)`
- `_glob2(dirname, pattern, dir_fd, dironly)`
- `_iterdir(dirname, dir_fd, dironly)`
- `_listdir(dirname, dir_fd, dironly)`
- `_rlistdir(dirname, dir_fd, dironly)`
- `_lexists(pathname, dir_fd)`

## gzip

- `write32u(output, value)`
- `read(self, size)`
- `seek(self, off)`
- `seekable(self)`
- `filename(self)`
- `mtime(self)`
- `__repr__(self)`
- `_init_write(self, filename)`
- `_write_gzip_header(self, compresslevel)`
- `write(self, data)`
- `peek(self, n)`
- `closed(self)`
- `close(self)`
- `fileno(self)`
  - Docstring: Invoke the underlying file object's fileno() method.

        This will raise AttributeError if the underlying file object
        doesn't support fileno().
- `rewind(self)`
- `readable(self)`
- `writable(self)`
- `seekable(self)`
- `__init__(self = None, fp = None)`
- `_init_read(self)`
- `_read_exact(self, n)`
- `_read_gzip_header(self)`
- `_add_read_data(self, data)`
- `_read_eof(self)`
- `_rewind(self = None)`
- `decompress(data)`
- `main()`

## header

- `decode_header(header)`
- `__str__(self)`
- `__eq__(self, other)`
- `_nonctext(self, s)`
- `_normalize(self)`
- `__init__(self, headerlen, maxlen, continuation_ws, splitchars)`
- `_str(self, linesep)`
- `__str__(self)`
- `newline(self)`
- `add_transition(self)`
- `feed(self, fws, string, charset)`
- `_maxlengths(self)`
- `_ascii_split(self, fws, string, splitchars)`
- `_append_chunk(self, fws, string)`
- `__init__(self = None, initial_size = None)`
- `push(self, fws, string)`
- `pop(self = None)`
- `__len__(self)`
- `__str__(self)`
- `is_onlyws(self)`
- `part_count(self = None)`

## headerregistry

- `display_name(self)`
- `username(self)`
- `domain(self)`
- `addr_spec(self)`
- `__repr__(self)`
- `__str__(self)`
- `__eq__(self, other)`
- `display_name(self)`
- `addresses(self)`
- `__repr__(self)`
- `__str__(self)`
- `__eq__(self, other)`
- `__new__(cls, name, value)`
- `init(self, name, *, parse_tree, defects)`
- `name(self)`
- `defects(self)`
- `__reduce__(self)`
- `_reconstruct(cls, value)`
- `fold(self, *, policy)`
- `_reconstruct_header(cls_name, bases, value)`
- `parse(cls, value, kwds)`
- `parse(cls, value, kwds)`
- `init(self = None, *args, **kw)`
- `datetime(self)`
- `value_parser(value)`
- `parse(cls, value, kwds)`
- `init(self = None, *args, **kw)`
- `groups(self)`
- `addresses(self)`
- `address(self)`
- `parse(cls, value, kwds)`
- `init(self = None, *args, **kw)`
- `major(self)`
- `minor(self)`
- `version(self)`
- `parse(cls, value, kwds)`

## inspect

- `get_annotations(obj = None, *, globals, locals, eval_str)`
- `ismodule(object)`
- `isclass(object)`
- `ismethod(object)`
- `ismethoddescriptor(object)`
- `isdatadescriptor(object)`
- `ismemberdescriptor(object)`
- `ismemberdescriptor(object)`
- `isgetsetdescriptor(object)`
- `isgetsetdescriptor(object)`
- `isfunction(object)`
- `_has_code_flag(f, flag)`
- `isgeneratorfunction(obj)`
- `iscoroutinefunction(obj)`
- `isasyncgenfunction(obj)`
- `isasyncgen(object)`
- `isgenerator(object)`
- `iscoroutine(object)`
- `isawaitable(object)`
- `istraceback(object)`
- `isframe(object)`
- `iscode(object)`
- `isbuiltin(object)`
- `isroutine(object)`
- `isabstract(object)`
- `classify_class_attrs(cls)`
- `getmro(cls)`
- `unwrap(func = None, *, stop)`
- `_is_wrapper(f)`
- `_is_wrapper(f = None)`

## install

- `__init__(self, translate_service)`
- `_on_manage(self)`
- `_on_accept(self)`
- `_on_decline(self)`
- `_on_open_link(self, url)`
- `wait_for_state(self)`
- `show(self)`
- `add_progress(self, msg)`
- `update_progress_text(self, msg)`
- `_clean_dialog(self)`
- `add_success_message(self, title, sub_title, msg)`
- `start_move(self, event)`
- `stop_move(self, event)`
- `on_drag(self, event)`

## ipaddress

- `ip_address(address)`
- `ip_interface(address)`
- `v4_int_to_packed(address)`
- `v6_int_to_packed(address)`
- `_split_optional_netmask(address)`
- `_find_address_range(addresses)`
- `_count_righthand_zero_bits(number, bits)`
- `summarize_address_range(first, last)`
- `_collapse_addresses_internal(addresses)`
- `collapse_addresses(addresses)`
- `get_mixed_type_key(obj)`
- `exploded(self)`
- `compressed(self)`
- `reverse_pointer(self)`
- `version(self)`
- `_check_int_address(self, address)`
- `_check_packed_address(self, address, expected_len)`
- `_ip_int_from_prefix(cls, prefixlen)`
- `_prefix_from_ip_int(cls, ip_int)`
- `_report_invalid_netmask(cls, netmask_str)`
- `_prefix_from_prefix_string(cls, prefixlen_str)`
- `_prefix_from_ip_string(cls, ip_str)`
- `_split_addr_prefix(cls, address)`
- `__reduce__(self)`
- `_explode_shorthand_ip_string(self)`
- `_make_netmask(cls, arg)`
- `_ip_int_from_string(cls, ip_str)`

## iterators

- `walk(self)`

## lzma

- `close(self)`
- `closed(self)`
- `fileno(self)`
- `seekable(self)`
- `readable(self)`
- `writable(self)`
- `write(self, data)`
- `tell(self)`

## machinery

- `all_suffixes()`

## numbers

- `__complex__(self)`
- `__bool__(self)`
- `real(self)`
- `imag(self)`
- `__add__(self, other)`
- `__radd__(self, other)`
- `__neg__(self)`
- `__pos__(self)`
- `__sub__(self, other)`
- `__rsub__(self, other)`
- `__mul__(self, other)`
- `__rmul__(self, other)`
- `__truediv__(self, other)`
- `__rtruediv__(self, other)`
- `__pow__(self, exponent)`
- `__rpow__(self, base)`
- `__abs__(self)`
- `conjugate(self)`
- `__eq__(self, other)`
- `__float__(self)`
- `__trunc__(self)`
- `__floor__(self)`
- `__ceil__(self)`
- `__divmod__(self, other)`
- `__rdivmod__(self, other)`
- `__floordiv__(self, other)`
- `__rfloordiv__(self, other)`
- `__mod__(self, other)`
- `__rmod__(self, other)`
- `__lt__(self, other)`
- `__le__(self, other)`
- `__complex__(self)`
- `real(self)`
- `imag(self)`
- `conjugate(self)`
- `numerator(self)`
- `denominator(self)`
- `__float__(self)`
- `__int__(self)`
- `__index__(self)`
- `__lshift__(self, other)`
- `__rlshift__(self, other)`
- `__rshift__(self, other)`
- `__rrshift__(self, other)`
- `__and__(self, other)`
- `__rand__(self, other)`
- `__xor__(self, other)`
- `__rxor__(self, other)`
- `__or__(self, other)`
- `__ror__(self, other)`
- `__invert__(self)`
- `__float__(self)`
- `numerator(self)`
- `denominator(self)`

## optparse

- `_repr(self)`

## parse

- `clear_cache()`
- `_noop(obj)`
- `_coerce_args(*args)`
- `username(self)`
- `password(self)`
- `hostname(self)`
- `port(self)`
- `_userinfo(self)`
- `_hostinfo(self)`
- `_userinfo(self)`
- `_hostinfo(self)`
- `geturl(self)`
- `geturl(self)`
- `geturl(self)`
- `geturl(self)`
- `geturl(self)`
- `geturl(self)`
- `_fix_result_transcoding()`
- `_splitparams(url)`
- `_checknetloc(netloc)`
- `_check_bracketed_netloc(netloc)`
- `_check_bracketed_host(hostname)`
- `urlunparse(components)`
- `urlunsplit(components)`
- `urldefrag(url)`
- `unquote_to_bytes(string)`
  - Docstring: unquote_to_bytes('abc%20def') -> b'abc def'.
- `__init__(self, safe)`
- `__repr__(self)`
- `__missing__(self, b)`

## parser

- `__init__(self, *args, **kw)`

## pathlib

- `_ignore_error(exception)`
- `_is_wildcard_pattern(pat)`
- `__init__(self)`
- `parse_parts(self, parts)`
- `join_parsed_parts(self, drv, root, parts, drv2, root2, parts2)`
- `casefold(self, s)`
- `casefold_parts(self, parts)`
- `compile_pattern(self, pattern)`
- `is_reserved(self, parts)`
- `make_uri(self, path)`
- `casefold(self, s)`
- `casefold_parts(self, parts)`
- `compile_pattern(self, pattern)`
- `is_reserved(self, parts)`
- `make_uri(self, path)`
- `link(self, src, dst)`
- `readlink(self, path)`
- `owner(self, path)`
- `group(self, path)`
- `_make_selector(pattern_parts, flavour)`
- `__init__(self, child_parts, flavour)`
- `select_from(self, parent_path)`
- `_select_from(self, parent_path, is_dir, exists, scandir)`
- `__init__(self, name, child_parts, flavour)`
- `_select_from(self, parent_path, is_dir, exists, scandir)`
- `__init__(self, pat, child_parts, flavour)`
- `_select_from(self, parent_path, is_dir, exists, scandir)`
- `__init__(self, pat, child_parts, flavour)`
- `_iterate_directories(self, parent_path, is_dir, scandir)`
- `_select_from(self, parent_path, is_dir, exists, scandir)`
- `__init__(self, path)`
- `__len__(self)`
- `__getitem__(self, idx)`
- `__repr__(self)`
- `__new__(cls, *args)`
- `__reduce__(self)`
- `_parse_args(cls, args)`
- `_from_parts(cls, args)`
- `_from_parsed_parts(cls, drv, root, parts)`
- `_format_parsed_parts(cls, drv, root, parts)`
- `_make_child(self, args)`
- `__str__(self)`
- `__fspath__(self)`
- `as_posix(self)`
- `__bytes__(self)`
- `__repr__(self)`
  - Docstring: Return the path as a 'file' URI.
- `as_uri(self)`
  - Docstring: Return the path as a 'file' URI.
- `_cparts(self)`
- `__eq__(self, other)`
- `__hash__(self)`
- `__lt__(self, other)`
- `__le__(self, other)`
- `__gt__(self, other)`
- `__ge__(self, other)`
- `__class_getitem__(cls, type)`
- `anchor(self)`
  - Docstring: The concatenation of the drive and root, or ''.
- `name(self)`
- `suffix(self)`
  - Docstring: The final component's last suffix, if any.

        This includes the leading period. For example: '.txt'
- `suffixes(self)`
  - Docstring: A list of the final component's suffixes, if any.

        These include the leading periods. For example: ['.tar', '.gz']
- `stem(self)`
- `with_name(self, name)`
- `with_stem(self, stem)`
- `with_suffix(self, suffix)`
- `relative_to(self, *other)`
- `is_relative_to(self, *other)`
- `parts(self)`
- `joinpath(self, *args)`
- `__truediv__(self, key)`
- `__rtruediv__(self, key)`
- `parent(self)`
- `parents(self)`
  - Docstring: A sequence of this path's logical parents.
- `is_absolute(self)`
- `is_reserved(self)`
- `match(self, path_pattern)`
- `__new__(cls, *args, **kwargs)`
- `_make_child_relpath(self, part)`
- `__enter__(self)`
- `__exit__(self, t, v, tb)`
- `cwd(cls)`
- `home(cls)`
  - Docstring: Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
- `samefile(self, other_path)`
- `iterdir(self)`
  - Docstring: Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
- `glob(self, pattern)`
- `rglob(self, pattern)`
- `absolute(self)`
- `check_eloop(e)`
- `stat(self = None, *, follow_symlinks)`
- `owner(self)`
- `group(self)`
- `read_bytes(self)`
- `write_bytes(self, data)`
- `readlink(self)`
- `chmod(self = None, mode = {
        'follow_symlinks': True }, *, follow_symlinks)`
- `lchmod(self, mode)`
  - Docstring: Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
- `rmdir(self)`
- `lstat(self)`
  - Docstring: Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
- `rename(self, target)`
- `replace(self, target)`

## platform

- `_comparable_version(version)`
- `win32_is_iot()`

## pprint

- `pp(object = None, *, sort_dicts, *args, **kwargs)`
- `saferepr(object)`
- `isreadable(object)`
- `isrecursive(object)`
- `__init__(self, obj)`
- `__lt__(self, other)`
- `_safe_tuple(t)`
- `pprint(self, object)`
- `pformat(self, object)`
- `isrecursive(self, object)`
- `isreadable(self, object)`
- `_format(self, object, stream, indent, allowance, context, level)`
- `_pprint_dataclass(self, object, stream, indent, allowance, context, level)`
- `_pprint_dict(self, object, stream, indent, allowance, context, level)`
- `_pprint_ordered_dict(self, object, stream, indent, allowance, context, level)`
- `_pprint_list(self, object, stream, indent, allowance, context, level)`
- `_pprint_tuple(self, object, stream, indent, allowance, context, level)`
- `_pprint_set(self, object, stream, indent, allowance, context, level)`
- `_pprint_str(self, object, stream, indent, allowance, context, level)`
- `_pprint_bytes(self, object, stream, indent, allowance, context, level)`
- `_pprint_bytearray(self, object, stream, indent, allowance, context, level)`
- `_pprint_mappingproxy(self, object, stream, indent, allowance, context, level)`
- `_pprint_simplenamespace(self, object, stream, indent, allowance, context, level)`
- `_format_dict_items(self, items, stream, indent, allowance, context, level)`
- `_format_namespace_items(self, items, stream, indent, allowance, context, level)`
- `_format_items(self, items, stream, indent, allowance, context, level)`
- `_repr(self, object, context, level)`
- `format(self, object, context, maxlevels, level)`
- `_pprint_default_dict(self, object, stream, indent, allowance, context, level)`
- `_pprint_counter(self, object, stream, indent, allowance, context, level)`
- `_pprint_chain_map(self, object, stream, indent, allowance, context, level)`
- `_pprint_deque(self, object, stream, indent, allowance, context, level)`
- `_pprint_user_dict(self, object, stream, indent, allowance, context, level)`
- `_pprint_user_list(self, object, stream, indent, allowance, context, level)`
- `_pprint_user_string(self, object, stream, indent, allowance, context, level)`
- `_safe_repr(self, object, context, maxlevels, level)`
- `_recursion(object)`
- `_wrap_bytes_repr(object, width, allowance)`

## py_compile

- `__str__(self)`
- `_get_default_invalidation_mode()`
- `main()`

## quoprimime

- `header_check(octet)`
- `body_check(octet)`
- `header_length(bytearray)`
- `body_length(bytearray)`
- `unquote(s)`
- `quote(c)`
- `_unquote_match(match)`
- `header_decode(s)`

## readers

- `remove_duplicates(items)`
- `__init__(self, loader)`
- `resource_path(self, resource)`
- `files(self)`
- `__init__(self, loader, module)`
- `open_resource(self = None, resource = None)`
- `is_resource(self, path)`
- `files(self)`
- `__init__(self, *paths)`
- `iterdir(self)`
- `read_bytes(self)`
- `read_text(self, *args, **kwargs)`
- `is_dir(self)`
- `is_file(self)`
- `joinpath(self, child)`
- `open(self, *args, **kwargs)`
- `name(self)`
- `__repr__(self)`
- `__init__(self, namespace_path)`
- `resource_path(self, resource)`
- `files(self)`

## selectors

- `_fileobj_to_fd(fileobj)`
- `__init__(self, selector)`
- `__len__(self)`
- `__getitem__(self, fileobj)`
- `__iter__(self)`
- `unregister(self, fileobj)`
- `close(self)`
- `get_key(self, fileobj)`

## shlex

- `punctuation_chars(self)`
- `push_token(self, tok)`
- `pop_source(self)`
- `get_token(self)`
  - Docstring: Get a token from the input stream (or from stack if it's nonempty)
- `read_token(self)`
- `sourcehook(self, newfile)`
- `__iter__(self)`
- `__next__(self)`
- `join(split_command)`
- `quote(s)`
- `_print_tokens(lexer)`

## signal

- `_int_to_enum(value, enum_klass)`
  - Docstring: Convert a numeric value to an IntEnum member.
    If it's not a known member, return the numeric value itself.
- `_enum_to_int(value)`
  - Docstring: Convert an IntEnum member to a numeric value.
    If it's not an IntEnum member return the value itself.
- `_wraps(wrapped)`
- `decorator(wrapper = None)`
- `signal(signalnum, handler)`
- `getsignal(signalnum)`
- `pthread_sigmask(how, mask)`
- `sigpending()`
- `sigwait(sigset)`
- `valid_signals()`

## statistics

- `_sum(data)`
- `_isfinite(x)`
- `_coerce(T, S)`
- `_exact_ratio(x)`
- `_convert(value, T)`
- `_find_lteq(a, x)`
- `_find_rteq(a, l, x)`
- `mean(data)`
- `fmean(data)`
- `geometric_mean(data)`
- `median(data)`
- `median_low(data)`
- `median_high(data)`
- `mode(data)`
- `multimode(data)`
- `quantiles(data = None, *, n, method)`
- `covariance(x, y)`
- `correlation(x, y)`
- `linear_regression(x, y)`
- `_normal_dist_inv_cdf(p, mu, sigma)`

## string

- `__init_subclass__(cls = None)`
- `__init__(self, template)`
- `_invalid(self, mo)`
- `convert(mo = None)`
- `convert(mo = None)`
- `format(self, format_string, *args, **kwargs)`
- `vformat(self, format_string, args, kwargs)`
- `get_value(self, key, args, kwargs)`
- `check_unused_args(self, used_args, args, kwargs)`
- `format_field(self, value, format_spec)`
- `convert_field(self, value, conversion)`
- `parse(self, format_string)`
- `get_field(self, field_name, args, kwargs)`

## textwrap

- `_munge_whitespace(self, text)`
- `_split(self, text)`
- `_fix_sentence_endings(self, chunks)`
- `_handle_long_word(self, reversed_chunks, cur_line, cur_len, width)`
- `_wrap_chunks(self, chunks)`
- `_split_chunks(self, text)`
- `wrap(self, text)`
- `fill(self, text)`
- `shorten(text, width, **kwargs)`
- `dedent(text)`
- `predicate(line)`
- `prefixed_lines()`

## tokenize

- `TokenInfo()`
- `__repr__(self)`
- `exact_type(self)`
- `group(*choices)`
- `any(*choices)`
- `maybe(*choices)`
- `_all_string_prefixes()`
- `_compile(expr)`

## tracemalloc

- `_format_size(size, sign)`
- `__init__(self, traceback, size, count)`
- `__hash__(self)`
- `__eq__(self, other)`
- `__str__(self)`
- `__repr__(self)`
- `_sort_key(self)`
- `__init__(self, traceback, size, size_diff, count, count_diff)`
- `__hash__(self)`
- `__eq__(self, other)`
- `__str__(self)`
- `__repr__(self)`
- `_sort_key(self)`
- `_compare_grouped_stats(old_group, new_group)`
- `get_object_traceback(obj)`
- `__init__(self, trace)`
- `domain(self)`
- `size(self)`
- `traceback(self)`
- `__eq__(self, other)`
- `__hash__(self)`
- `__str__(self)`
- `__repr__(self)`
- `__init__(self, traces)`
- `__len__(self)`
- `__getitem__(self, index)`
- `__contains__(self, trace)`
- `__eq__(self, other)`
- `__repr__(self)`
- `_normalize_filename(filename)`
- `__init__(self, inclusive)`
- `_match(self, trace)`
- `__init__(self = None, inclusive = None, filename_pattern = None, lineno = None, all_frames = None, domain = None)`
- `filename_pattern(self)`
- `_match_frame_impl(self, filename, lineno)`
- `_match_frame(self, filename, lineno)`
- `_match_traceback(self, traceback)`
- `_match(self, trace)`
- `__init__(self = None, inclusive = None, domain = None)`
- `domain(self)`
- `_match(self, trace)`
- `__init__(self, traces, traceback_limit)`
- `dump(self, filename)`
- `load(filename)`
- `_filter_trace(self, include_filters, exclude_filters, trace)`
- `filter_traces(self, filters)`
- `_group_by(self, key_type, cumulative)`
- `take_snapshot()`

## translate

- `__init__(self)`
- `get_lang(self)`

## ttk

- `_load_tile(master)`
- `_mapdict_values(items)`
- `_script_from_settings(settings)`
- `_list_from_statespec(stuple)`
- `_list_from_layouttuple(tk, ltuple)`
- `_val_or_dict(tk, options, *args)`
- `_convert_stringval(value)`
- `_to_number(x)`
- `_tclobj_to_py(val)`
- `tclobjs_to_py(adict)`
- `element_create(self, elementname, etype, *args, **kw)`
- `element_names(self)`
- `element_options(self, elementname)`
  - Docstring: Return the list of elementname's options.
- `theme_settings(self, themename, settings)`
- `theme_names(self)`
- `identify(self, x, y)`
- `invoke(self)`
- `invoke(self)`
- `bbox(self, index)`
- `identify(self, x, y)`
- `validate(self)`
- `set(self, value)`
- `add(self, child, **kw)`
- `forget(self, tab_id)`
- `hide(self, tab_id)`
- `identify(self, x, y)`
- `index(self, tab_id)`
- `insert(self, pos, child, **kw)`
- `tabs(self)`
- `enable_traversal(self)`
- `insert(self, pos, child, **kw)`
- `stop(self)`
- `invoke(self)`
- `set(self, value)`
- `set_children(self, item, *newchildren)`
- `delete(self, *items)`
- `detach(self, *items)`
- `exists(self, item)`
- `identify(self, component, x, y)`
- `identify_row(self, y)`
- `identify_column(self, x)`
- `identify_region(self, x, y)`
- `identify_element(self, x, y)`
- `index(self, item)`
  - Docstring: Returns the integer index of item within its parent's list
        of children.
- `move(self, item, parent, index)`
- `next(self, item)`
  - Docstring: Returns the identifier of item's next sibling, or '' if item
        is the last child of its parent.
- `parent(self, item)`
  - Docstring: Returns the ID of the parent of item, or '' if item is at the
        top level of the hierarchy.
- `prev(self, item)`
  - Docstring: Returns the identifier of item's previous sibling, or '' if
        item is the first child of its parent.
- `see(self, item)`
- `selection(self)`
- `_selection(self, selop, items)`
- `selection_set(self, *items)`
- `selection_add(self, *items)`
- `selection_remove(self, *items)`
- `selection_toggle(self, *items)`
- `destroy(self = None)`
- `_adjust(self, *args)`
- `adjust_label()`
- `value(self)`
- `value(self, val)`
- `__getitem__(self, item)`
- `destroy(self = None)`

## typing

- `_is_param_expr(arg)`
- `_type_repr(obj)`
- `_check_generic(cls, parameters, elen)`
- `_prepare_paramspec_params(cls, params)`
- `_deduplicate(params)`
- `_remove_dups_flatten(parameters)`
- `_flatten_literal_params(parameters)`
- `_tp_cache(func = None, *, typed)`
- `decorator(func = None)`
- `inner(*args, **kwds)`
- `__init_subclass__(self, *args, **kwds)`
- `__copy__(self)`
- `__deepcopy__(self, memo)`
- `__init__(self, getitem)`
- `__getattr__(self, item)`
- `__mro_entries__(self, bases)`
- `__repr__(self)`
- `__reduce__(self)`
- `__call__(self, *args, **kwds)`
- `__or__(self, other)`
- `__ror__(self, other)`
- `__instancecheck__(self, obj)`
- `__subclasscheck__(self, cls)`
- `__getitem__(self, parameters)`
- `__getitem__(self, parameters)`
- `Any(self, parameters)`
- `NoReturn(self, parameters)`
- `ClassVar(self, parameters)`
- `Final(self, parameters)`
- `Union(self, parameters)`
- `Optional(self, parameters)`
- `Literal(self, *parameters)`
- `TypeAlias(self, parameters)`
- `Concatenate(self, parameters)`

## utils

- `_has_surrogates(s)`
- `_sanitize(string)`
- `_iter_escaped_chars(addr)`
- `_strip_quoted_realnames(addr)`
- `getaddresses(fieldvalues = None, *, strict)`

## uu

- `test()`

## vdict

- `__iter__(self)`
- `__iter__(self)`
- `__iter__(self)`
- `__repr__(self)`
- `__len__(self)`
- `_verify_key_tuple(self, key)`
- `_normalize_key(self, key)`
- `__setitem__(self = None, key = None, value = None)`
- `__getitem__(self = None, key = None)`
- `__delitem__(self = None, key = None)`
- `__iter__(self)`
- `__contains__(self = None, key = None)`
- `__eq__(self, other)`
- `__ne__(self, other)`
- `clear(self = None)`
- `get(self = None, key = None, *args)`
- `pop(self, key)`
- `popitem(self)`
- `iterkeys(self)`
- `keys(self)`
- `itervalues(self)`
- `values(self)`
- `iteritems(self)`
- `items(self)`
- `get_all_for(self, key)`
- `remove_all_for(self = None, key = None)`
- `has_duplicates(self)`
- `dict_recurse(obj = None)`

## webbrowser

- `open_new(url)`
- `open_new_tab(url)`
- `_synthesize(browser = None, *, preferred)`
- `open_new(self, url)`
- `open_new_tab(self, url)`
- `__init__(self, name)`
- `_find_grail_rc(self)`
- `_remote(self, action)`
- `register_X_browsers()`
- `register_standard_browsers()`
- `__init__(self, name)`
- `__init__(self, name)`
- `main()`

