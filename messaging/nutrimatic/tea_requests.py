""""
File             : tea_requests.py
Author           : ian
Created          : 11-13-2016

Last Modified By : ian
Last Modified On : 11-13-2016
***********************************************************************
The MIT License (MIT)
Copyright © 2016 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
***********************************************************************
"""
from enum import Enum, unique


@unique
class BeverageType(Enum):
    tea = 0,
    coffee = 1


class TeaRequest:
    def __init__(self, beverage_type: int, has_milk: bool, no_of_sugars: int):
        self._beverage_type = beverage_type
        self._has_milk = has_milk
        self._no_of_sugars = no_of_sugars

    @property
    def beverage_type(self) -> BeverageType:
        return BeverageType(self._beverage_type)

    @property
    def has_milk(self) -> bool:
        return self._has_milk

    def no_of_sugars(self) -> int:
        return self._no_of_sugars