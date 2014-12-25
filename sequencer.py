import fileinput


def combine(sequence, read):
    """ Returns a tuple (combined_sequence, len(longest_overlap)), where combined_sequence is the combined substring
     given an overlap between sequence and read, and len(longest_overlap) is the length of the overlapping portion. If
     there is no overlap, combined_sequence will be None. The length of sequence must be at least the length of read,
     otherwise combine will return (None, 0).
    """
    if len(sequence) < len(read):
        return None, 0
    # if read in sequence:
    #     return sequence, len(read)

    longest_overlap = ""
    combined_sequence = None

    # find if read is a prefix/suffix of sequence
    for i in xrange(len(read)):
        read_end = read[i:]
        read_start = read[: len(read) - i]
        if sequence.startswith(read_end):
            longest_overlap = read_end
            combined_sequence = read + sequence.split(longest_overlap, 1)[1]
            break
        if sequence.endswith(read_start):
            longest_overlap = read_start
            combined_sequence = sequence + read.split(longest_overlap, 1)[1]
            break

    return combined_sequence, len(longest_overlap)


def main():
    reads = [read.strip() for read in fileinput.input()]
    sequence = max(reads, key=len)  # build up sequence, starting with longest read
    reads.remove(sequence)

    while reads:
        target_read = None  # want the read that gives maximum overlap -> minimum combined length
        target_subsequence = sequence
        longest_overlap_len = 0

        for read in reads:
            if read in sequence:
                reads.remove(read)

        for read in reads:
            subsequence, overlap_len = combine(sequence, read)
            if subsequence is not None and overlap_len >= longest_overlap_len:
                target_read = read
                target_subsequence = subsequence
                longest_overlap_len = overlap_len

        sequence = target_subsequence
        if target_read is not None:
            reads.remove(target_read)

    print sequence

if __name__ == "__main__":
    main()