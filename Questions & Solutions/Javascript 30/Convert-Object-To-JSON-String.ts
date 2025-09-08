/*
  If the object is null we return a string value of null,
  if it is an array we make a new array by mapping each element to a stringified version of it and join it into a string.
  If it is an object we map each key in the same way and if its a primitive we just return the String value.
*/

if (object === null) {
    return 'null';
  }

  if (Array.isArray(object)) {
    const elements = object.map((element: any) => jsonStringify(element));
    return `[${elements.join(',')}]`;
  }

  if (typeof object === 'object') {
    const keys = Object.keys(object);
    const keyValuePairs = keys.map((key: string) => `"${key}":${jsonStringify(object[key])}`);
    return `{${keyValuePairs.join(',')}}`;
  }

  if (typeof object === 'string') {
    return `"${object}"`;
  }

  return String(object);
