<?php

/*
 * This file is a part of the DiscordPHP-Http project.
 *
 * Copyright (c) 2021-present David Cole <david.cole1340@gmail.com>
 *
 * This file is subject to the MIT license that is bundled
 * with this source code in the LICENSE file.
 */

namespace Discord\Http\Exceptions;

/**
 * Thrown when a request to Discord's REST API returned ClientErrorResponse.
 *
 * @author SQKo
 */
class BadRequestException extends RequestFailedException
{
    protected $code = 400;
}
