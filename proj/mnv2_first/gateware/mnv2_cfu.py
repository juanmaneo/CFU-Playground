#!/bin/env python
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nmigen_cfu import InstructionBase, Cfu


class TemplateInstruction(InstructionBase):
    """Template instruction
    """

    def elab(self, m):
        with m.If(self.start):
            m.d.sync += self.output.eq(self.in0 + self.in1)
            m.d.sync += self.done.eq(1)
        with m.Else():
            m.d.sync += self.done.eq(0)


class Mnv2Cfu(Cfu):
    def __init__(self):
        super().__init__({
            0: TemplateInstruction(),
        })

    def elab(self, m):
        super().elab(m)


def make_cfu():
    return Cfu({
        # Add instructions here...
        0: TemplateInstruction(),
    })