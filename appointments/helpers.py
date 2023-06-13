# File: helpers.py
# Description: Various helper functions for views in the appointments app
# Author: Chris Knowles
# Date: Jun 2023


# Helper functions
def is_valid_nhs_number(nhs_number: str) -> bool:
    """
    :summary: Helper function to check a supplied NHS number for length of 10,
    that it represents an integer and that it passes the checksum validity as
    described at https://www.datadictionary.nhs.uk/attributes/nhs_number.html

    :param nhs_number: NHS number as string

    :return: True if valid NHS number, otherwise False as boolean
    """

    # Check if 10 digits in nhs_number, if not then return False
    if len(nhs_number) != 10:
        return False

    try:
        # Apply the weighting factors to each of the first 9 digits in the
        # nhs_number and sum this total
        weighting_factor = 10
        weighted_total = 0
        for digit in nhs_number[:9]:
            weighted_total += int(digit) * weighting_factor

            # Decrement weighting_factor for next digit
            weighting_factor -= 1

        # Use the weighted total to compare with the checksum for the
        # nhs_number
        rem = weighted_total % 11
        check_digit = 0 if (11 - rem) == 11 else (11 - rem)

        # Special condition if check_digit is 10 then the nhs_number is
        # invalid
        if check_digit == 10:
            return False

        # Now check the check_digit against the checksum (10 th digit in the
        # nhs_number, if they do not match then the nhs_number is checksum
        # invalid so return False
        checksum = int(nhs_number[9])
        if check_digit != checksum:
            return False
    except:
        # There is an error (of any type), typically this will be with the
        # form of the nhs_number (for instance it may not be of 10 integer
        # digits) so return False
        return False

    # All validation checks passed so return True
    return True


def coerce_postcode(postcode: str) -> str:
    """
    :summary: Helper function to coerce the supplied postcode to make it conform to the
    specification given in https://ideal-postcodes.co.uk/guides/uk-postcode-format, note
    this function does not attempt to validate a postcode, it only ensures that the
    returned postcode is compliant with the Outward Code and Inward Code form of a
    valid postcode

    :param postcode: postcode to coerce as string

    :return: coerced postcode as string
    """

    # Remove all whitespace from the postcode
    postcode = ''.join(postcode.split())

    # Insert whitespace ' ' after the Outward Code (which can be 2 to 4 characters long)
    # and before the Inward Code (which is always 3 characters long)
    # in length
    postcode = postcode[0:-3] + " " + postcode[-3:]

    return postcode
